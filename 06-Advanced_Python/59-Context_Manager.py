from contextlib import contextmanager


class File(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Will exit")
        return self.f.close()


@contextmanager
def another_open(path, mode):
    file = open(path, mode)
    yield file
    file.close()


with File("test.txt", "w") as f:
    print("Writing")
    f.write("Context test")

with another_open("test.txt", "a") as f:
    print("Continue to write")
    f.write("\nSimple context manager")
