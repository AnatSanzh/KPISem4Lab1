import json
from record import PhoneDirectoryRecord
from record_encoder import PhoneDirectoryRecordEncoder
from record_decoder import phone_directory_record_decoder
from abstract_storage import RecordStorage


class JsonRecordStorage(RecordStorage):
    """Class that can be used to interact with phone book record list. Saves data in json format"""
    def __init__(self, name: str):
        self.fileName = name
        with open(self.fileName, 'r') as myfile:
            self.records = json.loads(myfile.read(), object_hook=phone_directory_record_decoder)

    def add(self, number: str, name: str, address: str):
        """
        >>> [JsonRecordStorage("data/records_data.json").add("1234567890", "123", "123")]
        ['Record added successfully']

        The function adds a new record to the array and file
        :param number: number of new record
        :param name: name of new record
        :param address: address of new record
        :return: operation status
        """
        if self.get(number) is not None:
            return "A record with this number already exists."

        rec_to_add = PhoneDirectoryRecord(number, name, address)

        self.records.append(rec_to_add)

        self._save()

        return "Record added successfully"

    def get(self, number: str):
        """
        >>> [JsonRecordStorage.get(JsonRecordStorage("data/records_data.json"), "1111111234567890111111")]
        [None]

        The function finds an entry in the array
        :param number: number of the required record
        :return: record by number
        """
        return next((x for x in self.records if x.phone_number == number), None)

    def update(self, number: str, name: str, address: str):
        """
        >>> [JsonRecordStorage("data/records_data.json").update("1234567890111111", "123", "123")]
        ['Record not found']

====================
        HEAD
====================
        The function updates the record in the array and file
        :param number: number of record for update
        :param name: new name value
        :param address: new address value
        :return: operation status
====================
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

    def remove(self, number: str):
        """
        >>> [JsonRecordStorage("data/records_data.json").remove("123456789011111")]
        ['Record not found']

        >>> [JsonRecordStorage("data/records_data.json").remove("1234567890")]
        ['Record not found']

        #['Record successfully deleted']

        The function deletes the record from the file and the array
        :param number: number of record for delete
        :return: operation status
        """
        if self.get(number) is None:
            return "Record not found"

        self.records = [x for x in self.records if x.phone_number != number]
        self._save()

        return "Record successfully deleted"

    def _save(self):
        """

        The function saves data to file
        :return: None
        """
        with open(self.fileName, 'w') as myfile:
            myfile.write(json.dumps(self.records, cls=PhoneDirectoryRecordEncoder))

    def list(self, offset: int, count: int) -> list:
        """
        Returns slice of whole array of records

        :param offset: Offset from start
        :param count: Count of records
        :return: sublist depending on parameters
        """
        return self.records[offset:offset+count]

    def clear(self):
        """
        >>> [JsonRecordStorage("data/records_data.json").clear()]
        ['All records have been erased']

        The function to clear the array and file

        :return: operation status
        """
        self.records = []

        self._save()

        return "All records have been erased"


if __name__ == "__main__":
    import doctest
    doctest.testmod()


