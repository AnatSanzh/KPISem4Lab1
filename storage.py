import json
from record import PhoneDirectoryRecord
from record_encoder import PhoneDirectoryRecordEncoder
from record_decoder import phone_directory_record_decoder
import doctest


class JsonRecordStorage:
    """Class that can be used to interact with phone book record list. Saves data in json format"""
    def __init__(self, name: str):
        self.fileName = name
        with open(self.fileName, 'r') as myfile:
            self.records = json.loads(myfile.read(), object_hook=phone_directory_record_decoder)

    """The function adds a new record to the array and file"""
    def add(self, number: str, name: str, address: str):
        """
        >>> [JsonRecordStorage.add(JsonRecordStorage("data/records_data.json"), "1234567890", "123", "123")]
        ['Record added successfully']

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

    """the function finds an entry in the array"""
    def get(self, number: str):
        """
        >>> [JsonRecordStorage.get(JsonRecordStorage("data/records_data.json"), "1111111234567890111111")]
        [None]

        :param number:
        :return:
        """
        return next((x for x in self.records if x.phone_number == number), None)

    """the function updates the record in the array and file"""
    def update(self, number: str, name: str, address: str):
        """
        >>> [JsonRecordStorage.update(JsonRecordStorage("data/records_data.json"), "1234567890111111", "123", "123")]
        ['Record not found']


        :param number:
        :param name:
        :param address:
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

    """the function deletes the record from the file and the array"""
    def remove(self, number: str):
        """
        >>> [JsonRecordStorage.remove(JsonRecordStorage("data/records_data.json"), "123456789011111")]
        ['Record not found']

        >>> [JsonRecordStorage.remove(JsonRecordStorage("data/records_data.json"), "1234567890")]
        ['Record successfully deleted']

        :param number:
        :return:
        """
        if self.get(number) is None:
            return "Record not found"

        self.records = [x for x in self.records if x.phone_number != number]
        self._save()

        return "Record successfully deleted"

    """the function saves data to file"""
    def _save(self):
        """


        :return:
        """
        with open(self.fileName, 'w') as myfile:
            myfile.write(json.dumps(self.records, cls=PhoneDirectoryRecordEncoder))

    """the function returns a list of records"""
    def list(self, offset: int, count: int) -> list:
        """
        Returns slice of whole array of records

        :param offset: Offset from start
        :param count: Count of records
        :return:
        """
        return self.records[offset:offset+count]

    """function to clear the array and file"""
    def clear(self):
        """

        :return:
        """
        self.records = []

        self._save()

        return "All records have been erased"


doctest.testmod()


