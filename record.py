class PhoneDirectoryRecord:
    """Object that describes phone book record"""
    def to_string(self):
        """
        

        :return:
        """
        return "Phone number: " + self.phone_number + ", " +\
               "Name: " + self.name + ", " +\
               "Address: " + self.address + ";\n"

    def __init__(self, phone_number: str, name: str, address: str):
        self.phone_number = phone_number
        self.name = name
        self.address = address
