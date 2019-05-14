import storage


currentStorage = storage.JsonRecordStorage("data/records_data.json")


def get_records(offset: int, count: int) -> list:
    """
    Returns list of phone book records

    :param offset: From what positions start getting records
    :param count: Number of records to return
    :return: List with records
    """

    return []


def add_record():
    pass


def remove_record():
    pass


def update_record():
    pass


def remove_records_all():
    pass
