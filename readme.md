# pdb-dataset

We use data from the [Protein Data Bank (PDB)](https://www.rcsb.org/), a repository of experimentally determined structures available online.

## Data Representation

Full-atom, high-resolution structures are available in the PDB.

## Files and Their Functions

- `pdb_ids.txt` contains **115,850** IDs for the PDB files.
- `pdb_download.py`
  - Download each full-atom structure by its ID listed in `pdb_ids.txt`.
  - Generate `pdb_exceptions.txt` contains not downloaded IDs.
- `pdb_validate.py`
  - Trivial check of PDB file signature of incomplete downloaded files.
  - Generate `pdb_corrupted.txt` contains corrupted file IDs.

## References

- Anand, N., & Huang, P. (2018). *Generative modeling for protein structures*. <https://papers.nips.cc/paper/7978-generative-modeling-for-protein-structures>
- <https://github.com/collinarnett/protein_gan/tree/master/data>
