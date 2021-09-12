import dataclasses
import re
from collections import namedtuple

import specs


@dataclasses.dataclass
class FieldReader:
    """A reader for PDB fields.

    Used for reading PDB record segments. Holds information about start/end points and
    datatype. Provides a read method, that receives whole record (line) and returns
    the field.
    """

    name: str
    start: int
    end: int
    dtype: type

    def read(self, record):
        """Reads the field from record.

        Args:
          record: Full string of the record (PDB line).

        Returns:
          Parsed field. If the field is a string, it will be stripped from spaces. If
          it is a float or integer, it will be parsed into that float or integer.
        """

        frag = record[self.start : self.end]

        if self.dtype is str:
            return frag.strip()

        # Cast to dtype
        if frag.strip():
            return self.dtype(frag)

        return 0

    @staticmethod
    def get_dtype(raw_dtype):
        dtype_map = ((int, "integer"), (float, "real"))
        for python_type, pdb_type in dtype_map:
            if pdb_type in raw_dtype:
                return python_type
        return str

    @classmethod
    def from_pdb_description(cls, specline):
        """An alternative constructor for FieldReader class.

        This parses PDB record specifications; creates FieldReaders
        """

        def normalize_fragment(fragment):
            """Removes characters that are illegal to use in python variables."""
            chars_to_remove = re.compile(r"['\",:.[\](){} ]")
            return chars_to_remove.sub("", fragment).lower()

        # Normalize each fragment
        start_end, raw_dtype, name, *_ = [
            normalize_fragment(frag) for frag in specline.split("\t")
        ]

        start, *end = start_end.split("-")
        start = int(start)
        end = int(end[0] if end else start)
        dtype = cls.get_dtype(raw_dtype)

        return FieldReader(name, start, end, dtype)


class RecordReader:
    """Parses a PDB record into a namedtuple.

    A RecordReader has many FieldReaders to parse a PDB record. It also has a container
    that is made from a namedtuple to parse the PDB record into. Basically, if a PDB
    record is defined as follows:

       1-6  string "ATOM  " label
       7-8  string Symbol
       10-15 float  Mass

    Corresponding RecordReader will have 3 field readers for each of these fields. It
    will parse a line like:
      "ATOM  Fe 55.845"

    To:
      Atom(symbol: "Fe", mass: 55.845)

    Attributes:
      fields: A tuple of FieldReaders.
      container: A named tuple with names corresponding to field.name for fields.
    """

    def __init__(self, fields):
        """Creates a RecordReader from a sequence of FieldReaders.

        Args:
            fields: Instances of FieldReaders
        """
        self.name = fields[0].name.capitalize()
        self.fields = fields[1:]

        # Create a container for fields.
        self.container = namedtuple(self.name, [f.name for f in self.fields])

    @staticmethod
    def from_pdb_spec(spec):
        all_lines = (line.strip() for line in spec.splitlines())
        speclines = (line for line in all_lines if line)
        fields = [FieldReader.from_pdb_description(specline) for specline in speclines]
        return RecordReader(fields)

    def read(self, record):
        parsed_fields = {field.name: field.read(record) for field in self.fields}

        return self.container(**parsed_fields)

    def matches(self, record):
        return record.lower().startswith(self.name.lower())


Readers = {
    key: RecordReader.from_pdb_spec(spec) for key, spec in specs.ALL_SPECS.items()
}

types = {key: reader.container for key, reader in Readers.items()}
