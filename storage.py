import json
from record import PhoneDirectoryRecord
from record_encoder import PhoneDirectoryRecordEncoder
from record_decoder import phone_directory_record_decoder


class JsonRecordStorage:
    """Class that can be used to interact with phone book record list. Saves data in json format"""
    def __init__(self, name: str):
        self.fileName = name
        with open(self.fileName, 'r') as myfile:
            self.records = json.loads(myfile.read(), object_hook=phone_directory_record_decoder)

    def add(self, number: str, name: str, address: str):
        """


        :param number:
        :param name:
        :param address:
        :return:
        """
        if self.get(number) is not None:
            return "A record with this number already exists."

        rec_to_add = PhoneDirectoryRecord(number, name, address)

        self.records.append(rec_to_add)

        self._save()

        return "Record added successfully"

    def remove(self, number: str):
        """


        :param number:
        :return:
        """
        initial_size = len(self.records)
        self.records = [x for x in self.records if x.phone_number != number]

        self._save()
        if initial_size == len(self.records):
            return "Record successfully deleted"
        else:
            return "Record not found"

    def get(self, number: str):
        """


        :param number:
        :return:
        """
        return next((x for x in self.records if x.phone_number == number), None)

    def clear(self):
        """


        :return:
        """
        self.records = []

        self._save()

        return "Records removed"

    def _save(self):
        """


        :return:
        """
        with open(self.fileName, 'w') as myfile:
            myfile.write(json.dumps(self.records, cls=PhoneDirectoryRecordEncoder))

    def update(self, number: str, name: str, address: str):
        """


        :param number:
        :param new_record_data:
        :return:
        """
        new_record = PhoneDirectoryRecord(
            number,
            name,
            address
        )

        if self.get(number) is None:
            return "Record not found"

        self.records = [x if x.phone_number != number else new_record for x in self.records]

        self._save()

        return "Record successfully updated"

    def list(self, offset: int, count: int) -> list:
        """
        Returns slice of whole array of records

        :param offset: Offset from start
        :param count: Count of records
        :return:
        """
        return self.records[offset:offset+count]
