from storage import JsonRecordStorage

# import sys
# from enum import Enum

# class _CUIStates(Enum):
#    """Class that is used to track ConsoleInterface internal state"""
#    ISLE: int = 1
#    SHOW_RECORDS: int = 2


class ConsoleInterface:
    """Class that provides CUI that allows to interact with phone record list"""

    def __init__(self, storage: JsonRecordStorage):
        self.storage = storage

    def update(self):
        print("1. Show records \n2. Add record \n3. Remove records by phone number \n4. Erase all records")
        user_input = int(input())
        if user_input == 1:
            self.show_recs()
        elif user_input == 2:
            self.add_rec()
        elif user_input == 3:
            self.remove_rec()
        elif user_input == 4:
            self.remove_all_recs()

    def show_recs(self):
        for record in self.storage.records:
            record.write_record()

    def add_rec(self):
        print("Write phone number:")
        add_phone_number_input = input()
        print("Write name of the record:")
        add_name_input = input()
        print("Write address:")
        add_address_input = input()
        self.storage.add(add_phone_number_input, add_name_input, add_address_input)

    def remove_rec(self):
        print("Write phone number:")
        remove_phone_number_input = input()
        self.storage.remove(remove_phone_number_input)

    def remove_all_recs(self):
        print("All records have been erased")
        del self.storage.records[0: len(self.storage.records)]

    def run(self):
        while True:
            self.update()
