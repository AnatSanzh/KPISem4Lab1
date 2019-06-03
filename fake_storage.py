from record import PhoneDirectoryRecord
from abstract_storage import RecordStorage


class MemoryRecordStorage(RecordStorage):
    """Class that can be used to test functions that rely on real storage"""
    def __init__(self, initial_list: list = []):
        self.records = initial_list

    def add(self, number: str, name: str, address: str) -> str:
        """
        >>> MemoryRecordStorage().add("+38","name","addr")
        'Record added successfully'


        The function adds a new record to the array

        :param number: number of new record
        :param name: name of new record
        :param address: address of new record
        :return: operation status
        """
        if self.get(number) is not None:
            return "A record with this number already exists."

        rec_to_add = PhoneDirectoryRecord(number, name, address)

        self.records.append(rec_to_add)

        return "Record added successfully"

    def remove(self, number: str) -> str:
        """
        >>> MemoryRecordStorage().remove("1111111234567890111111")
        'Record not found'

        The function finds and removes an entry from the array
        :param number: number of the required record
        :return: operation status
        """
        if self.get(number) is None:
            return "Record not found"

        self.records = [x for x in self.records if x.phone_number != number]

        return "Record successfully deleted"

    def get(self, number: str) -> PhoneDirectoryRecord:
        """
        >>> MemoryRecordStorage(
        ... [ PhoneDirectoryRecord("num","nam","adr") ]
        ... ).get("num").__dict__
        {'phone_number': 'num', 'name': 'nam', 'address': 'adr'}

        The function finds an entry in the array
        :param number: number of the required record
        :return: record by number
        """
        return next(
            (x for x in self.records if x.phone_number == number),
            None)

    def clear(self) -> str:
        """
        >>> MemoryRecordStorage().clear()
        'All records have been erased'

        The function to clear the array and file
        :return: operation status
        """
        self.records = []

        return "All records have been erased"

    def update(self, number: str, name: str, address: str) -> str:
        """
        >>> MemoryRecordStorage().update("1234567890111111", "123", "123")
        'Record not found'

        The function updates the record in the array and file

        :param number: number of record for update
        :param name: new name value
        :param address: new address value
        :return: operation status
        """
        if self.get(number) is None:
            return "Record not found"

        new_record = PhoneDirectoryRecord(
            number,
            name,
            address
        )
        self.records = [
            x if x.phone_number != number else new_record for x in self.records
        ]

        return "Record successfully updated"

    def list(self, offset: int, count: int) -> list:
        """
        >>> MemoryRecordStorage(
        ... [ PhoneDirectoryRecord("a","b","c"),
        ... PhoneDirectoryRecord("v","b","n") ]).list(1,2)[0].__dict__
        {'phone_number': 'v', 'name': 'b', 'address': 'n'}

        Returns slice of whole array of records.

        :param offset: Offset from start
        :param count: Count of records
        :return: sublist depending on parameters
        """
        return self.records[offset:offset+count]
