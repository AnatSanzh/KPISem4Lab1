import json
import record


class PhoneDirectoryRecordEncoder(json.JSONEncoder):
    def default(self, obj):
        """


        :param obj:
        :return:
        """
        if isinstance(obj, record.PhoneDirectoryRecord):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
