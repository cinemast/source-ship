import re


class ChangeLog:
    def __init__(self, filename):
        version_re = re.compile("^## \[[a-zA-Z]*([0-9]+\.?){0,}[0-9]+\]")
        self.unreleased_re = re.compile("^## \[unreleased\]", re.IGNORECASE)
        with open(filename, "r") as file:
            self.entries = []
            entry = []
            for line in file:
                if version_re.match(line) or self.unreleased_re.match(line):
                    entry = [line.strip(), ""]
                    self.entries.append(entry)
                elif len(entry) > 0:
                    entry[1] += line

    def is_dirty(self):
        for entry in self.entries:
            if self.unreleased_re.match(entry[0]):
                return True
        return False

    def get_entry(self, version):
        for entry in self.entries:
            if version in entry[0]:
                return entry
        return []
