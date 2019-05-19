"""
This file contains flask server implementation that provides API for records.
"""

from flask import Flask
from flask_restful import reqparse, Resource, Api


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
            return storage.get(record_number)

        def put(self, record_number):
            return storage.update(record_number, _update_record_parser.parse_args())

        def delete(self, record_number):
            return storage.remove(record_number)

    return _RecordResource


def _get_records_resource_class(storage):
    class _RecordsResource(Resource):
        def post(self):
            return storage.add(_add_record_parser.parse_args())

        def delete(self):
            return storage.clear()

    return _RecordsResource


class Server:
    """Class that allows to interact with phone book over Internet"""
    def __init__(self, storage):
        self._underlying_app = Flask(__name__)
        self._underlying_app.debug = False

        self._api = Api(self._underlying_app)
        self._api.add_resource(_get_record_resource_class(storage), '/record/<str:record_number>')
        self._api.add_resource(_get_records_resource_class(storage), '/records')

    def run(self):
        self._underlying_app.run()
