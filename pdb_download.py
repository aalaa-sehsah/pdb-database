# Reference: https://github.com/collinarnett/protein_gan

from pathlib import Path
from urllib import request
import os


def download_pdb_file(db_dir: Path, id_: str, force: bool):
    DB_LINK = "http://files.rcsb.org/download/{id}.pdb"
    path_ = db_dir / f"{id_}.pdb"
    temp = f"{path_}.temp"

    if not force and path_.exists():
        return True

    try:
        request.urlretrieve(DB_LINK.format(id=id_), temp)
        os.rename(temp, path_)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    import argparse
    from utils import LoadingBar

    parser = argparse.ArgumentParser(description="Download PDB files from wwPDB.org")
    parser.add_argument(
        "--input_list",
        "-i",
        help="Input text file of IDs to download",
        type=str,
        default="pdb_ids.txt",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output path of downloaded files",
        type=str,
        default="pdb",
    )
    parser.add_argument(
        "--retries", "-r", help="Failed retries of each ID", type=int, default=3
    )
    parser.add_argument(
        "--log",
        "-l",
        help="Output file of not downloaded IDs",
        type=str,
        default="pdb_exceptions.txt",
    )
    parser.add_argument(
        "--force",
        "-f",
        help="Force overwrite if found",
        default=False,
        action="store_true",
    )
    args = parser.parse_args()

    arg_ids_list: str = args.input_list
    arg_db_dir: str = args.output
    arg_retries: int = args.retries
    arg_exceptions: str = args.log
    arg_force: bool = args.force

    # Step #1: Get train IDs list
    try:
        ids_list = Path(arg_ids_list).read_text().splitlines()
    except FileNotFoundError as _:
        print(f"[FATAL] ids_list: '{arg_ids_list}' is not found")
        exit(1)

    # Step #2: Create database directory
    try:
        db_dir = Path(arg_db_dir)
        db_dir.mkdir(exist_ok=True)
    except FileNotFoundError as _:
        print(f"[FATAL] db_dir: '{arg_db_dir}' is not found")
        exit(1)

    # Step #3: Download files and append exceptions
    exceptions = []
    bar = LoadingBar(len(ids_list))
    for i, id_ in enumerate(ids_list):
        # Step #3.1: Retry if file failed to download
        for trial in range(arg_retries):
            ok = download_pdb_file(db_dir, id_, arg_force)

            if not ok and trial == 0:
                exceptions.append(id_)
            else:
                break
        bar.update(i)
    bar.finish()

    # Step #4: Save exceptions to a file
    if exceptions:
        try:
            with open(arg_exceptions, "w+") as fp:
                fp.write("\n".join(exceptions))
            text = f"{len(exceptions)} entries" if len(exceptions) != 1 else "(1 entry)"
            print(f"[INFO] Exceptions file containing ({text}) has been created!")
        except Exception as e:
            print(f"[ERROR] {e}")
            exit(1)
    else:
        print("[INFO] All files are downloaded successfully.")
