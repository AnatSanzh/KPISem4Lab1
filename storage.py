import json, record

class JsonRecordStorage:
    records = []
    fileName = ""

    def add(self, title, content):
        recToAdd = record.LibraryRecord()
        recToAdd.content = content
        recToAdd.title = title

    def remove(self, title):
        pass

    def get(self, title):
        pass

    def load(self, name):
        pass