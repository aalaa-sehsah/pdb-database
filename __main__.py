from pathlib import Path
from urllib import request


def parse_pdb_ids_file(filepath: str) -> list[str]:
    try:
        return Path(filepath).read_text().splitlines()
    except Exception as e:
        print(f"[FATAL] {e}")
        exit(1)


def create_pdb_dir(dirpath: str) -> Path:
    try:
        db_dir = Path(dirpath)
        db_dir.mkdir(exist_ok=True)
        return db_dir
    except Exception as e:
        print(f"[FATAL] {e}")
        exit(1)


def download_pdb_files(
    pdb_ids: list[str],
    db_dir: Path,
    exceptions_filepath: str,
    overwrite: bool,
) -> list[str]:
    # PDB file signature (used for validation)
    SIGNATURE = (f"END{' '* 77}\n").encode("ASCII")

    def check_file(filepath: str, num_letters: int = len(SIGNATURE)) -> bool:
        with open(filepath, "rb") as file:
            file.seek(0, 2)
            filesize = file.tell()
            file.seek(-num_letters, 2)
            return file.read(num_letters) == SIGNATURE and filesize > 1000

    def download_file(db_dir: Path, id_: str, overwrite: bool = False) -> bool:
        DB_LINK = "http://files.rcsb.org/download/{id}.pdb"
        filepath = db_dir / f"{id_}.pdb"
        temp_filepath = filepath.parent / (filepath.name + ".temp")

        if not overwrite and filepath.exists():
            return check_file(filepath)

        try:
            request.urlretrieve(DB_LINK.format(id=id_), temp_filepath)
            temp_filepath.rename(filepath)
            return check_file(filepath)
        except Exception as e:
            print(f"[ERROR] ({id_}) {e}")
            return False

    exceptions: list[str] = []
    count = len(pdb_ids)
    for i, id_ in enumerate(pdb_ids, start=1):
        print(f"[INFO] File {i:,}/{count:,}", end="\r")
        status = download_file(db_dir, id_, overwrite)
        if status is False:
            exceptions.append(id_)
    print(f"[INFO] Finished Download of {count:,} PDB files")

    # Save exceptions list
    try:
        with open(exceptions_filepath, "w+") as fp:
            fp.write("\n".join(exceptions))
        print(f"[INFO] {len(exceptions)} Exceptions")
    except Exception as e:
        print(f"[FATAL] {e}")
        exit(1)


if __name__ == "__main__":
    import os

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    import argparse

    parser = argparse.ArgumentParser(
        description="A script to download PDB files (train/test files)"
    )

    parser.add_argument(
        "--mode",
        type=str,
        choices=["train", "test"],
        default="train",
        help="mode of operation: 'train', 'test'",
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="overwrite already downloaded files",
    )

    args = parser.parse_args()

    # Script arguments
    mode: str = args.mode
    overwrite: str = args.overwrite

    # ------------------------------------------------------------------------ #
    pdb_ids_filename = f"pdb_{mode}_ids.txt"
    pdb_output_dirname = f"pdb_{mode}"
    exceptions_filename = f"pdb_{mode}_exceptions.txt"

    pdb_ids = parse_pdb_ids_file(filepath=pdb_ids_filename)
    output_dir = create_pdb_dir(dirpath=pdb_output_dirname)

    download_pdb_files(
        pdb_ids=pdb_ids,
        db_dir=output_dir,
        exceptions_filepath=exceptions_filename,
        overwrite=overwrite,
    )
