from storage import JsonRecordStorage


class ConsoleInterface:
    """Class that provides CUI that allows to interact with phone record list"""

    def __init__(self, storage: JsonRecordStorage):
        self.storage = storage
        self.active = True
        self.switcher = {
            1: self.show_recs,
            2: self.add_rec,
            3: self.update_rec,
            4: self.remove_rec,
            5: self.remove_all_recs
        }

    def update(self):
        """


        :return:
        """
        print("\n1. Show records \n2. Add record \n3. Update record\n4. Remove records by phone number \n5. Erase all records \nEnter the command >>> ")
        user_input = int(input())

        func = self.switcher.get(user_input, lambda: "Invalid command")
        print(func())

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
            return string_of_records;

    def add_rec(self):
        """


        :return:
        """
        print("Write phone number:")
        add_phone_number_input = input()
        print("Write name of the record:")
        add_name_input = input()
        print("Write address:")
        add_address_input = input()
        return self.storage.add(add_phone_number_input, add_name_input, add_address_input)

    def remove_rec(self):
        """


        :return:
        """
        print("Write phone number:")
        remove_phone_number_input = input()
        return self.storage.remove(remove_phone_number_input)

    def remove_all_recs(self):
        """


        :return:
        """
        print("All records have been erased")
        return self.storage.clear()

    def update_rec(self):
        """


        :return:
        """
        print("Write phone number:")
        update_phone_number_input = input()
        print("Write new name of the record:")
        update_name_input = input()
        print("Write new address:")
        update_address_input = input()
        return self.storage.update(update_phone_number_input, update_name_input, update_address_input)

    def run(self):
        """


        :return:
        """
        while self.active:
            self.update()
