from v1.modules.singleton import Singleton


class Settings(metaclass=Singleton):
    def __init__(self):
        self.version = None
        pass

    def set_version(self, version):
        self.version = version