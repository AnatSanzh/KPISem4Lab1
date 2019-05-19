from storage import JsonRecordStorage
import record


currentStorage = JsonRecordStorage("data/records_data.json")


def get_records(offset: int, count: int) -> list:
    """
    Returns list of phone book records

    :param offset: From what positions start getting records
    :param count: Number of records to return
    :return: List with records
    """
    if len(currentStorage.records) > offset + count + 1:
        return currentStorage.records[offset:offset + count + 1]
    else:
        return currentStorage.records[offset:len(currentStorage.records)]


def add_record(new_record: record):
    currentStorage.records.append(new_record)
    pass


def remove_record(phone_number: str):
    for cur_record in currentStorage.records:
        if cur_record.phone_number == phone_number:
            currentStorage.records.remove(cur_record)
            break
    pass


def update_record(phone_number: int, new_record: record):
    for cur_record in currentStorage.records:
        if cur_record.phone_number == phone_number:
            currentStorage.records[currentStorage.records.index(cur_record)] = new_record
            break
    pass


def remove_records_all():
    currentStorage.records = []
    pass
