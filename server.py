from flask import Flask, request
from flask_restful import Resource, Api


"""class RecordResource(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
"""


class Server:
    """Class that allows to interact with phone book over Internet"""
    def __init__(self):
        self._underlying_app = Flask(__name__)
        self._underlying_app.debug = False

        self._api = Api(self._underlying_app)
        #self._api.add_resource(TodoSimple, '/<:todo_id>')

    def run(self):
        self._underlying_app.run()
