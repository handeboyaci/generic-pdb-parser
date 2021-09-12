import unittest
import record_reader

RecordReader = record_reader.RecordReader
FieldReader = record_reader.FieldReader


class TestRecordRecord(unittest.TestCase):
    def setUp(self) -> None:
        self.record1 = "ATOM    294 2HG  GLU    18     -13.518  -3.769   0.084  1.00  0.00           H"
        self.record2 = (
            "CRYST1   52.000   58.600   61.900  90.00  90.00  90.00 P 21 21 21    8 "
        )
        spec = """
        1 - 6	Record name	"ATOM"
        7 - 11	Integer	serial	Atomserial number.
        13 - 16	Atom	name	Atom name.
        17	Character	altLoc	Alternate location indicator.
        18 - 20	Residue name 	resName	Residue name.
        22	Character	chainID	Chain identifier.
        23 - 26	Integer	resSeq	Residue sequence number.
        27	AChar	iCode	Code for insertion of residues.
        31 - 38	Real(8.3)	x	Orthogonal coordinates for X in Angstroms.
        39 - 46	Real(8.3)	y	Orthogonal coordinates for Y in Angstroms.
        47 - 54	Real(8.3)	z	Orthogonal coordinates for Z in Angstroms.
        55 - 60	Real(6.2)	occupancy 	Occupancy.
        61 - 66	Real(6.2)	tempFactor	Temperaturefactor.
        77 - 78	LString(2)	element	Element symbol, right-justified.
        79 - 80	LString(2)	charge	Chargeon the atom. """
        self.record_reader = RecordReader.from_pdb_spec(spec)

    def test_record_reader_matches(self):
        self.assertTrue(self.record_reader.matches(self.record1))

    def test_record_reader_not_match(self):
        self.assertFalse(self.record_reader.matches(self.record2))

    def test_record_reader_read(self):
        parsed = self.record_reader.read(self.record1)
        self.assertEqual(parsed.name, "HG")
        self.assertEqual(parsed.serial, 294)
        self.assertEqual(parsed.x, -13.518)
        self.assertEqual(parsed.occupancy, 1.00)
        self.assertEqual(parsed.element, "H")


class TestFieldReader(unittest.TestCase):
    def setUp(self):
        specline1 = "17	Character	altLoc	Alternate location indicator"
        specline2 = "23 - 26	Integer	resSeq	Residue sequence number."
        specline3 = "31 - 38	Real(8.3)	x	Orthogonal coordinates for X in Angstroms."
        self.field_reader1 = FieldReader.from_pdb_description(specline1)
        self.field_reader2 = FieldReader.from_pdb_description(specline2)
        self.field_reader3 = FieldReader.from_pdb_description(specline3)

    def test_name(self):
        self.assertEqual(self.field_reader3.name, "x")

    def test_start_end_both_given(self):
        self.assertEqual(self.field_reader2.start, 23)
        self.assertEqual(self.field_reader2.end, 26)

    def test_start_no_end_given(self):
        self.assertEqual(self.field_reader1.start, 17)
        self.assertEqual(self.field_reader1.end, 17)

    def test_dtype_integer(self):
        self.assertEqual(self.field_reader2.dtype, int)

    def test_dtype_float(self):
        self.assertEqual(self.field_reader3.dtype, float)

    def test_dtype_str(self):
        self.assertEqual(self.field_reader1.dtype, str)


if __name__ == "__main__":
    unittest.main()
