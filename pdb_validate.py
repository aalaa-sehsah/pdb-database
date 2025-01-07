"""This script only checks the END string in each PDB file"""

SIGNATURE = (f"END{' '* 77}\n").encode("ASCII")


def check_signature(file_path: str, num_letters: int = 81) -> bool:
    """Check PDB file signature"""

    with open(file_path, "rb") as file:
        file.seek(0, 2)
        filesize = file.tell()
        file.seek(-num_letters, 2)
        return file.read(num_letters) == SIGNATURE and filesize > 1000


if __name__ == "__main__":
    import os
    from utils import LoadingBar

    BASE_DIR = "pdb"
    filenames = []
    corrupted = []

    # Step #1: Get current filenames
    print("[INFO] Get downloaded files")
    for _, _, filenames in os.walk(BASE_DIR):
        filenames = [i for i in filenames if i.lower().endswith(".pdb")]
        break

    # Step #2: Loop over files and validate them
    print("[INFO] Validate downloaded files")
    bar = LoadingBar(len(filenames), 0.1)
    for i, fn in enumerate(filenames):
        if not check_signature(f"{BASE_DIR}/{fn}"):
            corrupted.append(fn)
        bar.update(i)
    bar.finish()

    # Step #3: Report corrupted files
    if corrupted:
        with open("pdb_corrupted.txt", "w+") as fp:
            fp.write("\n".join([i[:-4] for i in corrupted]))
        text = f"{len(corrupted)} entries" if len(corrupted) != 1 else "1 entry"
        print(f"[INFO] Corrupted file containing ({text}) has been created!")
    else:
        print("[INFO] No corrupted files were found")
