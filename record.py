class PhoneDirectoryRecord:
    """Object that describes phone book record"""
    def write_record(self):
        """
        

        :return:
        """
        print("Phone number: "+self.phone_number, end=",")
        print("Name: "+self.name, end=",")
        print("Address: "+self.address, end=";")

    def __init__(self, phone_number: str, name: str, address: str):
        self.phone_number = phone_number
        self.name = name
        self.address = address
