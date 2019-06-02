"""
This file contains flask server implementation that provides API for records.
"""

from flask import Flask
from flask_restful import reqparse, Resource, Api
import json
from record_encoder import PhoneDirectoryRecordEncoder
import logging
from threading import Thread
from fake_storage import MemoryRecordStorage
from record import PhoneDirectoryRecord


_add_record_parser = reqparse.RequestParser()
_add_record_parser.add_argument("number", type=str)
_add_record_parser.add_argument("address", type=str)
_add_record_parser.add_argument("name", type=str)

_update_record_parser = reqparse.RequestParser()
_update_record_parser.add_argument("address", type=str)
_update_record_parser.add_argument("name", type=str)

_list_records_parser = reqparse.RequestParser()
_list_records_parser.add_argument("offset", type=int)
_list_records_parser.add_argument("count", type=int)


def _get_record_resource_class(storage):
    """
    >>> _get_record_resource_class(MemoryRecordStorage([ PhoneDirectoryRecord("a","b","c") ]))().get("a")
    '{"phone_number": "a", "name": "b", "address": "c"}'

    >>> memory = MemoryRecordStorage([ PhoneDirectoryRecord("a","b","c") ])
    >>> _get_record_resource_class(memory)().delete("a")
    >>> memory.get("a")


    Factory method that produces classes that invoke operations on
    distinct records.

    :param storage: reference to the storage where entities are stored
    :return: class that contains HTTP request method handlers
    """
    class _RecordResource(Resource):
        def get(self, record_number: str) -> str:
            """
            Returns record by number.

            :param record_number: Phone number of record to return
            :return: JSON data of record encoded into string
            """
            return json.dumps(storage.get(record_number), cls=PhoneDirectoryRecordEncoder)

        def put(self, record_number):
            """
            Modifies records properties by number

            :param record_number: Phone number of record
            :return: Nothing
            """
            parsed_args = _update_record_parser.parse_args()
            storage.update(record_number, parsed_args['name'], parsed_args['address'])

        def delete(self, record_number):
            """
            Removes records properties by number

            :param record_number: Phone number of record
            :return: Nothing
            """
            storage.remove(record_number)

    return _RecordResource


def _get_records_resource_class(storage):
    """
    >>> memory = MemoryRecordStorage([ PhoneDirectoryRecord("a","b","c") ])
    >>> _get_records_resource_class(memory)().delete()
    >>> memory.get("a")


    Factory method that produces classes that invoke operations on
    whole record list.

    :param storage: reference to the storage where entities are stored
    :return: class that contains HTTP request method handlers
    """
    class _RecordsResource(Resource):
        def get(self):
            """
            Returns list of records of length 'count' from position 'offset'.

            :return: JSON data of record list encoded into string
            """
            parsed_args = _list_records_parser.parse_args()
            list_to_send = storage.list(parsed_args["offset"], parsed_args["count"])
            return json.dumps(list_to_send, cls=PhoneDirectoryRecordEncoder)

        def post(self):
            """
            Creates new record and adds it to list.

            :return: Nothing
            """
            parsed_args = _add_record_parser.parse_args()
            storage.add(parsed_args["number"], parsed_args["name"], parsed_args["address"])

        def delete(self):
            """
            Deletes all records.

            :return: Nothing
            """
            storage.clear()

    return _RecordsResource


def _server_worker_function(app: Flask):
    """
    Function that starts flask server.

    :param app: Flask server that will be started
    :return: Nothing
    """
    app.run()


class Server:
    """Class that allows to interact with phone book over Internet"""
    def __init__(self, storage, debug=False):
        self._underlying_app = Flask(__name__)
        self._underlying_app.debug = debug

        self._api = Api(self._underlying_app)
        self._api.add_resource(_get_record_resource_class(storage), '/record/<string:record_number>')
        self._api.add_resource(_get_records_resource_class(storage), '/records')

    def run(self):
        """
        Function that starts server in another thread.
        Also disables server log.

        :return: Nothing.
        """
        self._underlying_app.logger.disabled = True
        log = logging.getLogger('werkzeug')
        log.disabled = True

        thread = Thread(
            target=_server_worker_function,
            args=(self._underlying_app,)
        )

        thread.start()

    def get_app(self):
        """
        Returns underlying server app.

        :return: underlying flask app
        """
        return self._underlying_app
