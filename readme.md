# pdb-database

We use data from the [Protein Data Bank (PDB)](https://www.rcsb.org/), a repository of experimentally determined structures available online.

## Data Representation

Full-atom, high-resolution structures are available in the PDB.

## Files and Their Functions

- `__main__.py`
  - Download each full-atom structure by its ID listed in `pdb_ids.txt`.
  - Generate `pdb_exceptions.txt` contains not downloaded IDs.
- `pdb_ids.txt` contains **115,850** IDs for the PDB files.

## References

- Anand, N., & Huang, P. (2018). *Generative modeling for protein structures*. <https://papers.nips.cc/paper/7978-generative-modeling-for-protein-structures>
- <https://github.com/collinarnett/protein_gan/tree/master/data>
