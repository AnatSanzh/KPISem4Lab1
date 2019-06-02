from storage import JsonRecordStorage


class ConsoleInterface:
    """Class that provides CUI that allows to interact with phone record list"""

    def __init__(self, storage: JsonRecordStorage):
        self.storage = storage
        self.switcher = {
            1: self.show_recs,
            2: self.add_rec,
            3: self.update_rec,
            4: self.remove_rec,
            5: self.remove_all_recs
        }

    """function outputs console interface and responds user input"""
    def update(self):
        """


        :return:
        """
        print("\n1. Show records"
              "\n2. Add record"
              "\n3. Update record"
              "\n4. Remove records by phone number"
              "\n5. Erase all records"
              "\nEnter the command >>> ")

        while True:
            try:
                user_input = int(input())
                if user_input < 1 or user_input > 4:
                    raise ValueError  # this will send it to the print message and back to the input option
                break
            except ValueError:
                print("Invalid integer. The number must be in the range of 1-10.")

        func = self.switcher.get(user_input, lambda: "Invalid command")
        print(func())

    """function implements interface that outputs all records"""
    def show_recs(self):
        """


        :return:
        """
        if len(self.storage.records) == 0:
            return "Records not found!"
        else:
            string_of_records = ""
            for record in self.storage.records:
                string_of_records += record.to_string()
            return string_of_records

    """function implements interface that adds record"""
    def add_rec(self):
        """
        >>> [ConsoleInterface.add_rec(ConsoleInterface())]
        ['Record added successfully']


        :return:
        """
        print("Write phone number:")
        add_phone_number_input = input()
        print("Write name of the record:")
        add_name_input = input()
        print("Write address:")
        add_address_input = input()
        return self.storage.add(add_phone_number_input, add_name_input, add_address_input)

    """function implements interface that removes record"""
    def remove_rec(self):
        """
        >>> [ConsoleInterface.remove_rec(ConsoleInterface())]
        ['Record not found']


        :return:
        """
        print("Write phone number:")
        remove_phone_number_input = input()
        return self.storage.remove(remove_phone_number_input)

    """function implements interface that removes all records"""
    def remove_all_recs(self):
        """
        >>> [ConsoleInterface.remove_rec(ConsoleInterface())]
        ['All records have been erased']


        :return:
        """
        return self.storage.clear()

    """function implements interface that updates record"""
    def update_rec(self):
        """
        >>> [ConsoleInterface.update_rec(ConsoleInterface())]
        ['Record successfully updated']


        :return:
        """
        print("Write phone number:")
        update_phone_number_input = input()
        print("Write new name of the record:")
        update_name_input = input()
        print("Write new address:")
        update_address_input = input()
        return self.storage.update(update_phone_number_input, update_name_input, update_address_input)

    """function runs loop for infinite menu output"""
    def run(self):
        """


        :return:
        """
        while True:
            self.update()
