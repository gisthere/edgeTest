import socket


class Socket:

    def __new__(cls, address, port):
        if not hasattr(cls, 'connections'):
            cls.connections = {}
        new_connection = Connection(address, port)
        if new_connection not in cls.connections:
            cls.connections[new_connection] = new_connection
        return cls.connections[new_connection]


class Connection:

    def __init__(self, address: str, port: int, buffer_size: int = 1024):
        self.address = address
        self.port = port
        self.buffer_size = buffer_size
        self.connection = None

    def __eq__(self, other: 'Connection'):
        return self.address == other.address and self.port == other.port

    def __hash__(self):
        result = 0
        for c in self.address:
            result += ord(c)
        result += self.port
        return result

    def __str__(self):
        return f'{self.address}:{self.port}'

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        if self.connection:
            self.connection.close()
            self.connection = None

    def open(self):
        self.__exit__()
        if self.connection is None:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.address, self.port))
            self.connection = s

    def send(self, message: bytes):
        if not self.connection:
            self.open()

        self.connection.send(message)

    @property
    def can_send(self):
        return bool(self.connection)