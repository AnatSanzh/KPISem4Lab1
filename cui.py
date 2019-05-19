from storage import JsonRecordStorage
import os

# import sys
# from enum import Enum

# class _CUIStates(Enum):
#    """Class that is used to track ConsoleInterface internal state"""
#    ISLE: int = 1
#    SHOW_RECORDS: int = 2


class ConsoleInterface:
    """Class that provides CUI that allows to interact with phone record list"""

#    state = _CUIStates.ISLE
#    state_data = {}

    def update(self):
        print("1. Show records")
        print("2. Add record")
        print("3. Remove records by phone number")
        print("4. Erase all records")
        user_input = int(input())
        json_record_obj = JsonRecordStorage("data/records_data.json")
        if user_input == 1:
            for record in JsonRecordStorage.records:
                record.write_record()
        elif user_input == 2:
            print("Write phone number:")
            add_phone_number_input = input()
            print("Write name of the record:")
            add_name_input = input()
            print("Write address:")
            add_address_input = input()
            JsonRecordStorage.add(json_record_obj, add_phone_number_input, add_name_input, add_address_input)
        elif user_input == 3:
            print("Write phone number:")
            remove_phone_number_input = input()
            JsonRecordStorage.remove(json_record_obj, remove_phone_number_input)
        elif user_input == 4:
            print("All records have been erased")
            del JsonRecordStorage.records[0 : len(JsonRecordStorage.records)]
        pass

    def run(self):
        while True:
            self.update()
        """Starts CUI"""
        # todo: implement!!!
        """
            starts infinite loop that calls _update function
            maybe in another thread
        """
        pass
