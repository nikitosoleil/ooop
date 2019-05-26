# singleton
class Config:
    __instance = None

    def __new__(cls):
        if Config.__instance is None:
            Config.__instance = object.__new__(Config)
        return Config.__instance

    def __init__(self):
        self.batch_size = 128
