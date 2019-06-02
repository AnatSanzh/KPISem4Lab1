from record import PhoneDirectoryRecord


def phone_directory_record_decoder(dct) -> PhoneDirectoryRecord:
    """


    :param dct:
    :return:
    """
    return PhoneDirectoryRecord(
        dct['phone_number'],
        dct['name'],
        dct['address']
    )
