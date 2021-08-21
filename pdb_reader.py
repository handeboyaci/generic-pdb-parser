import record_reader


class PDBReader:
    def __init__(self, filename, readers=tuple(record_reader.Readers.values())):
        self.filename = filename
        self.readers = readers
        self.f = None
        self.reset()

    def close(self):
        if self.f and not self.f.closed:
            self.f.close()

    def reset(self):
        if not self.f or self.f.closed:
            self.f = open(self.filename)
        self.f.seek(0)

    def __enter__(self):
        self.reset()
        return self

    def __exit__(self, type, value, traceback):
        self.close()
        return False

    def _read_matching_record(self, record):
        for reader in self.readers:
            if reader.matches(record):
                return reader.read(record)

        return None

    def __next__(self):
        return next(iter(self))

    def __iter__(self):
        for line in self.f:
            record = self._read_matching_record(line)

            if record:
                yield record
