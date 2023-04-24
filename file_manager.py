import os

from student import Student


class FileManager:
    def __init__(self, file):
        self.file = file

    def save_data(self, data):
        with open(self.file, "w") as f:
            for d in data:
                f.write("{} {} {} {}\n".format(d.name, d.id, d.gender, d.score))

    def read_data(self):
        if not os.path.exists(self.file):
            return []

        with open(self.file, "r") as f:
            lines = f.readlines()

        data = []
        for line in lines:
            name, id, gender, score = line.strip().split(" ")
            data.append(Student(name, id, gender, score))
        return data