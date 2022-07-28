import json


class TextFile:
    def read(self, file):
        with open(file) as f:
            return f.readlines()

    def write(self, file, lines):
        pass

class JSONFile:
    def read(self, file):
        with open(file) as f:
            return json.load(f)

    def write(self, file, lines):
        pass



file1 = JSONFile()

data = file1.read('text.json')

print(data)
