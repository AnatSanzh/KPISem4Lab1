import json, record


class JsonRecordStorage:
    def __init__(self, name):
        self.fileName = name
        with open('data.txt', 'r') as myfile:
            self.records = json.loads(myfile.read())

    def add(self, title, content):
        rec_to_add = record.LibraryRecord()
        rec_to_add.content = content
        rec_to_add.title = title

        self.records.append(rec_to_add)

        self.save()

    def remove(self, title):
        self.records = [x for x in self.records if x.tittle == title]

        self.save()

    def get(self, title):
        return next((x for x in self.records if x.title == title), None)

    def clear(self):
        self.records = []
        self.save()

    def save(self):
        with open(self.fileName, 'w') as myfile:
            myfile.write(json.dumps(self.records))
