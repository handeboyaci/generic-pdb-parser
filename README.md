# A Hacky PDB parser

This is a toy PDB parser that learns how to parse a PDB record from official specifications [here](https://www.wwpdb.org/documentation/file-format-content/format23/sect9.html
). If a record type is not supported, just add it to the `ALL_SPECS` dictionary in `spec.py`; `tab`-separate the columns and it can read that too.

`1.pdb` is an example pdb file with different record types. Clone the repo & `python main.py` to see it at work.
