import record


def phone_directory_record_decoder(dct):
    return record.PhoneDirectoryRecord(
        dct['phone_number'],
        dct['name'],
        dct['address']
    )
