from server import Server
from cui import ConsoleInterface
from storage import JsonRecordStorage
import time

storage = JsonRecordStorage("data/records_data.json")

server_app = Server(storage)
console_app = ConsoleInterface(storage)

if __name__ == '__main__':
    server_app.run()
    time.sleep(0.1)
    console_app.run()
