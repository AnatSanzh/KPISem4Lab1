from json import JSONEncoder
from record import PhoneDirectoryRecord


class PhoneDirectoryRecordEncoder(JSONEncoder):
    def default(self, obj):
        """
        >>> PhoneDirectoryRecordEncoder.default(None, PhoneDirectoryRecord("+390","that","there"))
        {'phone_number': '+390', 'name': 'that', 'address': 'there'}


        This function is used in order to serialize record to JSON.

        :param obj: record object to serialize
        :return: serialized record in JSON format
        """
        if isinstance(obj, PhoneDirectoryRecord):
            return obj.__dict__
        return JSONEncoder.default(self, obj)
