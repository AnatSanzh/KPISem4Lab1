class PhoneDirectoryRecord:
    """Object that describes phone book record"""

    def __init__(self, phone_number: str, name: str, address: str):
        self.phone_number = phone_number
        self.name = name
        self.address = address
