from typing import Iterator

from driver import Driver


class ListNode:
    def __init__(self, value):
        self.__value = value
        self.__l = self.__r = None

    def link(self, ln: 'ListNode'):
        self.__r = ln
        ln.__l = self

    @property
    def value(self):
        return self.__value

    @property
    def l(self):
        return self.__l

    @property
    def r(self):
        return self.__r


class CustomList(Driver):
    def __init__(self):
        self.__head = None
        self.__len = 0

    def __add(self, ln: ListNode):
        if self.__head:
            self.__head.l.link(ln)
        else:
            self.__head = ln
        ln.link(self.__head)
        self.__len += 1

    def add(self, value):
        ln = ListNode(value)
        self.__add(ln)

    def __remove(self, ln: ListNode):
        if self.__len == 1:
            self.__head = None
        elif self.__head == ln:
            self.__head = ln.r
        ln.l.link(ln.r)
        self.__len -= 1

    def remove(self, value):
        found = self.__find(value)
        if found:
            self.__remove(found)

    def __find(self, value):
        cur_node = self.__head
        while True:
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.r
            if cur_node == self.__head:
                return None

    def find(self, value):
        if self.__len > 0:
            found = self.__find(value)
            if found:
                return found.value
        return None

    @property
    def head(self):
        return self.__head

    def __len__(self):
        return self.__len

    def __iter__(self):  # pattern: factory method
        return ListIterator(self)


class ListIterator(Iterator):  # iterator
    def __init__(self, l: CustomList):
        self.__list = l
        self.__cur_node = l.head
        self.__flag = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cur_node == self.__list.head and self.__flag:
            raise StopIteration
        result = self.__cur_node
        self.__cur_node = self.__cur_node.r
        self.__flag = True
        return result.value
