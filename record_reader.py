import dataclasses
import re
from collections import namedtuple

import specs


class PDBDataType:
    """A class to convert PDB datatypes to python datatypes

    This class does simple mapping between the datatypes described in PDB specs and
    python datatypes, such as:

        Char      -> str
        Real(6,3) -> float
        Integer   -> int
    """

    dtype_map = ((int, "integer"), (float, "real"))

    @classmethod
    def get_dtype(cls, string):
        for python_type, pdb_type in cls.dtype_map:
            if pdb_type in string:
                return python_type
        return str


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
        self.container = namedtuple(
            self.name,
            [f.name for f in fields[1:]],
        )

    @classmethod
    def from_pdb_description(cls, text):
        """An alternative constructor for RecordReader class.

        This parses PDB record specifications; creates FieldReaders and container
        that is appropriate for that specification.
        """
        all_lines = (line.strip() for line in text.splitlines())

        # Drop empty lines
        lines = (line for line in all_lines if line)

        def normalize_fragment(fragment):
            """Removes characters that are illegal to use in python variables."""
            chars_to_remove = re.compile(r"['\",:.[\](){} ]")
            return chars_to_remove.sub("", fragment).lower()

        # Then split each line, and normalize each fragment
        splitted_lines = (
            [normalize_fragment(frag) for frag in line.split("\t")] for line in lines
        )

        # Now create field readers
        fields = []
        for start_end, pdb_type, field, *_ in splitted_lines:

            if "-" in start_end:
                # Parse instances like: 1 - 6
                start, end = [int(num) for num in start_end.split("-")]
            else:
                # Parse instance like: 17
                start = int(start_end)
                end = start

            # Get data type of the field
            dtype = PDBDataType.get_dtype(pdb_type)

            fields.append(FieldReader(field, start - 1, end, dtype))

        return RecordReader(tuple(fields))

    def read(self, record):
        parsed_fields = {field.name: field.read(record) for field in self.fields}

        return self.container(**parsed_fields)

    def matches(self, record):
        return record.lower().startswith(self.name.lower())


Readers = {
    key: RecordReader.from_pdb_description(spec)
    for key, spec in specs.ALL_SPECS.items()
}

types = {key: reader.container for key, reader in Readers.items()}
