from abstract_storage import RecordStorage
from fake_storage import MemoryRecordStorage
from io import StringIO
import sys


def io_helper_set_new(in_str: str):  # pragma: no cover
    temp = [sys.stdin, sys.stdout]

    sys.stdin = StringIO(in_str)
    sys.stdout = StringIO()

    return temp


def io_helper_set_former(io_streams):  # pragma: no cover
    sys.stdin = io_streams[0]
    sys.stdout = io_streams[1]


_choices = "\n1. Show records" \
            "\n2. Add record " \
            "\n3. Update record" \
            "\n4. Remove records by phone number" \
            "\n5. Erase all records " \
            "\nEnter the command >>> "


class ConsoleInterface:
    """
    Class that provides CUI that allows to interact with phone record list
    """

    def __init__(self, storage: RecordStorage):
        self.storage = storage
        self.switcher = {
            1: self.show_recs,
            2: self.add_rec,
            3: self.update_rec,
            4: self.remove_rec,
            5: self.remove_all_recs
        }

    def update(self):  # pragma: no cover
        """

        function outputs console interface and responds user input
        :return: one of 5 results on user`s choice
        """
        print(_choices)

        while True:
            try:
                user_input = int(input())
                if user_input < 1 or user_input > 5:
                    raise ValueError
                    # this will send it to the
                    # print message and back to the input option
                break
            except ValueError:
                print("Invalid integer. "
                      "The number must be in the range of 1-5.")

        func = self.switcher.get(user_input, lambda: "Invalid command")
        print(func())

    def show_recs(self):
        """

        function implements interface that outputs all records
        :return: a string to which all records are appended
        """
        if len(self.storage.records) == 0:
            return "Records not found!"
        else:
            string_of_records = ""
            for record in self.storage.records:
                string_of_records += record.to_string()
            return string_of_records

    def add_rec(self):
        """
        >>> temp = io_helper_set_new("12\\nname\\naddr\\n")
        >>> val= ConsoleInterface(MemoryRecordStorage([])).add_rec()
        >>> io_helper_set_former(temp)
        >>> val
        'Record added successfully'


        function implements interface that adds record
        :return: adds record to the storage and saves it
        """
        print("Write phone number:")
        add_phone_number_input = input()
        print("Write name of the record:")
        add_name_input = input()
        print("Write address:")
        add_address_input = input()
        return self.storage.add(
            add_phone_number_input, add_name_input, add_address_input
        )

    def remove_rec(self):
        """
        >>> temp = io_helper_set_new("12\\n")
        >>> res= ConsoleInterface(MemoryRecordStorage()).remove_rec()
        >>> io_helper_set_former(temp)
        >>> res
        'Record not found'


        function implements interface that removes record
        :return: removes a record from the storage and saves it
        """
        print("Write phone number:")
        remove_phone_number_input = input()
        return self.storage.remove(remove_phone_number_input)

    def remove_all_recs(self):
        """
        >>> [ConsoleInterface(MemoryRecordStorage()).remove_all_recs()]
        ['All records have been erased']


        function implements interface that removes all records
        :return: clears the storage and saves it
        """
        return self.storage.clear()

    def update_rec(self):
        """
        >>> temp = io_helper_set_new("12\\nname\\naddr\\n")
        >>> res= ConsoleInterface(MemoryRecordStorage()).update_rec()
        >>> io_helper_set_former(temp)
        >>> res
        'Record not found'


        function implements interface that updates record
        :return: rewrites the chosen record in the storage to the input data
        """
        print("Write phone number:")
        update_phone_number_input = input()
        print("Write new name of the record:")
        update_name_input = input()
        print("Write new address:")
        update_address_input = input()
        return self.storage.update(
            update_phone_number_input, update_name_input, update_address_input
        )

    def run(self):  # pragma: no cover
        """


        function runs loop for infinite menu output
        :return: infinitely shows the choices
        """
        while True:
            self.update()
