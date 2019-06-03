class PhoneDirectoryRecord:
    """Object that describes phone book record"""
    def to_string(self):
        """
        Convert object to string
        >>> [PhoneDirectoryRecord("123", "123", "123").to_string()]
        ['Phone number: 123, Name: 123, Address: 123\\n']

        :return: string
        """
        return "Phone number: " + self.phone_number + ", " +\
               "Name: " + self.name + ", " +\
               "Address: " + self.address + "\n"

    def __init__(self, phone_number: str, name: str, address: str):
        self.phone_number = phone_number
        self.name = name
        self.address = address


if __name__ == "__main__":
    import doctest
    doctest.testmod()
