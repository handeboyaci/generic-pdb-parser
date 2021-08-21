import record_reader
from pdb_reader import PDBReader


def print_header(message):
    print()
    print("#" * (len(message) + 6))
    print("## " + message + " ##")
    print("#" * (len(message) + 6))
    print()


# Can choose some record readers to use and others will be ignored.
# Otherwise all the registered readers will be tried.
readers_to_use = [
    record_reader.Readers["Cryst1"],
    record_reader.Readers["Atom"],
    record_reader.Readers["Hetatm"],
    # record_reader.Readers["Siguij"],
]


# with PDBReader("1.pdb", readers_to_use) as pdb:
with PDBReader("1.pdb") as pdb:
    x = y = z = counter = 0

    # Parse records
    print_header("Parsing and outputting PDB records.")
    for record in pdb:

        # Print parsed record
        print(record)

        # Aggregate data if record is an Atom
        if isinstance(record, record_reader.types["Atom"]):
            x += record.x
            y += record.y
            z += record.z
            counter += 1

print_header("Some example calculation")

print(
    "Center of mass (assuming all atoms have same mass!) = "
    f"{x / counter:.2f}, {y/counter:.2f}, {z/counter:.2f}"
)
