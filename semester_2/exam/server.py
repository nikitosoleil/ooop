from typing import List


class Server:
    def __init__(self, name: str, ip: str, connections: List['Server']):
        self.name = name
        self.ip = ip
        self.connections = connections
