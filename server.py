"""
This file contains flask server implementation that provides API for records.
"""

from flask import Flask
from flask_restful import reqparse, Resource, Api
import json
from record_encoder import PhoneDirectoryRecordEncoder


_add_record_parser = reqparse.RequestParser()
_add_record_parser.add_argument("number", type=str)
_add_record_parser.add_argument("address", type=str)
_add_record_parser.add_argument("name", type=str)

_update_record_parser = reqparse.RequestParser()
_update_record_parser.add_argument("address", type=str)
_update_record_parser.add_argument("name", type=str)


def _get_record_resource_class(storage):
    class _RecordResource(Resource):
        def get(self, record_number):
            return json.dumps(storage.get(record_number), cls=PhoneDirectoryRecordEncoder)

        def put(self, record_number):
            storage.update(record_number, _update_record_parser.parse_args())

        def delete(self, record_number):
            storage.remove(record_number)

    return _RecordResource


def _get_records_resource_class(storage):
    class _RecordsResource(Resource):
        def post(self):
            parsed_args = _add_record_parser.parse_args()
            storage.add(parsed_args["number"], parsed_args["name"], parsed_args["address"])

        def delete(self):
            storage.clear()

    return _RecordsResource


class Server:
    """Class that allows to interact with phone book over Internet"""
    def __init__(self, storage):
        self._underlying_app = Flask(__name__)
        self._underlying_app.debug = True

        self._api = Api(self._underlying_app)
        self._api.add_resource(_get_record_resource_class(storage), '/record/<string:record_number>')
        self._api.add_resource(_get_records_resource_class(storage), '/records')

    def run(self):
        self._underlying_app.run()
