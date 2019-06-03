from record import PhoneDirectoryRecord


def phone_directory_record_decoder(dct) -> PhoneDirectoryRecord:
    """
    >>> phone_directory_record_decoder(
    ... { "phone_number": "+30", "name": "thing", "address": "lake" }
    ... ).to_string()
    'Phone number: +30, Name: thing, Address: lake\\n'

    This function is used in order to deserialize record from JSON.

    :param dct: dictionary that represents JSON object
    :return: deserialized record
    """
    return PhoneDirectoryRecord(
        dct['phone_number'],
        dct['name'],
        dct['address']
    )
