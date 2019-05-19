import json
import record


class JsonRecordStorage:
    """Class that can be used to interact with phone book record list. Saves data in json format"""
    def __init__(self, name: str):
        self.fileName = name
        with open(self.fileName, 'r') as myfile:
            self.records = json.loads(myfile.read())

    def add(self, number: str, name: str, address: str):
        """
        Adds record to storage.

        :param number:
        :param name:
        :param address:
        :return:
        """
        rec_to_add = record.PhoneDirectoryRecord()
        rec_to_add.phone_number = number
        rec_to_add.name = name
        rec_to_add.address = address

        self.records.append(rec_to_add)

        self._save()

    def remove(self, number: str):
        """Removes record from storage by """
        self.records = [x for x in self.records if x.phone_number == number]

        self._save()

    def get(self, number: str):
        return next((x for x in self.records if x.phone_number == number), None)

    def clear(self):
        self.records = []
        self._save()

    def _save(self):
        with open(self.fileName, 'w') as myfile:
            myfile.write(json.dumps(self.records))

    def update(self, number: str, data: object):
        # todo: implement!!!
        pass
