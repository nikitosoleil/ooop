from driver import Driver


class BuiltinList(Driver):  # pattern: adapter
    def __init__(self):
        self.__list = []

    def add(self, value):
        self.__list.append(value)

    def remove(self, value):
        if value in self.__list:
            self.__list.remove(value)

    def find(self, value):
        for candidate in self.__list:
            if candidate == value:
                return candidate
        return None

    def __len__(self):
        return len(self.__list)

    def __iter__(self):
        return iter(self.__list)
