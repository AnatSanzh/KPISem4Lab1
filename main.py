from server import Server
from cui import ConsoleInterface

server_app = Server()
console_app = ConsoleInterface()

if __name__ == '__main__':
    server_app.run()
    console_app.run()
