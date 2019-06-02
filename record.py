class PhoneDirectoryRecord:
    """Object that describes phone book record"""
    def write_record(self):
        """
        >>> PhoneDirectoryRecord("+30", "thing", "lake").write_record()
        Phone number: +30,
        Name: thing,
        Address: lake;

        Prints record information to console

        :return: Nothing
        """
        temp_str = "Phone number: "+self.phone_number+",\nName: "+self.name+",\nAddress: "+self.address+";"
        print(temp_str)

    def __init__(self, phone_number: str, name: str, address: str):
        self.phone_number = phone_number
        self.name = name
        self.address = address
