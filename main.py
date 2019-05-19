from server import Server
from cui import ConsoleInterface
from storage import JsonRecordStorage

storage = JsonRecordStorage("data/records_data.json")

server_app = Server(storage)
console_app = ConsoleInterface(storage)

if __name__ == '__main__':
    server_app.run()
    console_app.run()
