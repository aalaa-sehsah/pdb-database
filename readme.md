# pdb-database

We use data from the [Protein Data Bank (PDB)](https://www.rcsb.org/), a repository of experimentally determined structures available online.

Each file is downloaded using `http://files.rcsb.org/download/{id}.pdb`, where IDs are stored in `pdb_train_ids.txt` and `pdb_test_ids.txt`.

## Data Representation

Full-atom, high-resolution structures are available in the PDB.

## Environment

- VS Code
- Python 3.12

## Files and Their Functions

- `__main__.py`
  - Download each full-atom structure using **train** or **test** data list.
  - Generate exceptions files contains not downloaded IDs.
  - Validate downloaded files; if it is run for the second time.
- `pdb_train_ids.txt` contains **115,850** IDs for the train PDB files.
- `pdb_test_ids.txt` contains **6,248** IDs for the test PDB files.

## Usage Guidelines

In the terminal, change directory to the folder where the repo is located. Type the following:
- On Windows: `python {command}`
- On Linux/MacOS: `python3 {command}`

Commands Examples:
- `pdb-database --help` - Show script help
- `pdb-database --mode=train` - download train data (default without arguments)
- `pdb-database --mode=test` - download test data

## References

- Anand, N., & Huang, P. (2018). *Generative modeling for protein structures*. <https://papers.nips.cc/paper/7978-generative-modeling-for-protein-structures>
- <https://github.com/collinarnett/protein_gan/tree/master/data>
