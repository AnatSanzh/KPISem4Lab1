import json
from record import PhoneDirectoryRecord


class JsonRecordStorage:
    """Class that can be used to interact with phone book record list. Saves data in json format"""
    def __init__(self, name: str):
        self.fileName = name
        with open(self.fileName, 'r') as myfile:
            self.records = json.loads(myfile.read())

    def add(self, number: str, name: str, address: str):
        rec_to_add = PhoneDirectoryRecord(number, name, address)

        self.records.append(rec_to_add)

        self._save()

    def remove(self, number: str):
        self.records = [x for x in self.records if x.phone_number != number]

        self._save()

    def get(self, number: str):
        return next((x for x in self.records if x.phone_number == number), None)

    def clear(self):
        self.records = []

        self._save()

    def _save(self):
        with open(self.fileName, 'w') as myfile:
            myfile.write(json.dumps(self.records))

    def update(self, number: str, new_record: PhoneDirectoryRecord):
        self.records = [x if x.phone_number != number else new_record for x in self.records]
        pass
