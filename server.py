"""
This file contains flask server implementation that provides API for records.
"""

from flask import Flask
from flask_restful import reqparse, Resource, Api
import json
from record_encoder import PhoneDirectoryRecordEncoder
import logging
import threading


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


    :param storage:
    :return:
    """
    class _RecordResource(Resource):
        def get(self, record_number):
            """


            :param record_number:
            :return:
            """
            return json.dumps(storage.get(record_number), cls=PhoneDirectoryRecordEncoder)

        def put(self, record_number):
            """


            :param record_number:
            :return:
            """
            storage.update(record_number, _update_record_parser.parse_args())

        def delete(self, record_number):
            """


            :param record_number:
            :return:
            """
            storage.remove(record_number)

    return _RecordResource


def _get_records_resource_class(storage):
    """


    :param storage:
    :return:
    """
    class _RecordsResource(Resource):
        def get(self):
            """


            :return:
            """
            parsed_args = _list_records_parser.parse_args()
            list_to_send = storage.list(parsed_args["offset"], parsed_args["count"])
            return json.dumps(list_to_send, cls=PhoneDirectoryRecordEncoder)

        def post(self):
            """


            :return:
            """
            parsed_args = _add_record_parser.parse_args()
            storage.add(parsed_args["number"], parsed_args["name"], parsed_args["address"])

        def delete(self):
            """


            :return:
            """
            storage.clear()

    return _RecordsResource


def _server_worker_function(app):
    """


    :param app:
    :return:
    """
    app.run()


class Server:
    """Class that allows to interact with phone book over Internet"""
    def __init__(self, storage):
        self._underlying_app = Flask(__name__)
        self._underlying_app.debug = False

        self._api = Api(self._underlying_app)
        self._api.add_resource(_get_record_resource_class(storage), '/record/<string:record_number>')
        self._api.add_resource(_get_records_resource_class(storage), '/records')

    def run(self):
        """


        :return:
        """
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        thread = threading.Thread(
            target=_server_worker_function,
            args=(self._underlying_app,)
        )

        thread.start()
