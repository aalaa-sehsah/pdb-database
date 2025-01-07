# pdb-database

We use data from the [Protein Data Bank (PDB)](https://www.rcsb.org/), a repository of experimentally determined structures available online.

## Data Representation

Full-atom, high-resolution structures are available in the PDB.

## Environment

- VS Code
- Python 3.12

## Files and Their Functions

- `__main__.py`
  - Download each full-atom structure by its ID listed in `pdb_ids.txt`.
  - Generate `pdb_exceptions.txt` contains not downloaded IDs.
  - Validate downloaded files; if it is run for the second time.
- `pdb_ids.txt` contains **115,850** IDs for the PDB files.
- `pdb_exceptions.txt` currently contains 15 entries.

## References

- Anand, N., & Huang, P. (2018). *Generative modeling for protein structures*. <https://papers.nips.cc/paper/7978-generative-modeling-for-protein-structures>
- <https://github.com/collinarnett/protein_gan/tree/master/data>
