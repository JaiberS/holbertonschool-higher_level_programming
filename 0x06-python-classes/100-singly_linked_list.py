#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if not type(data) == int:
            raise TypeError('data must be an integer')
        if next_node is not None or not type(next_node) == Node:
            raise TypeError('next_node must be a Node Object')
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not type(value) == int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or not type(value) == Node:
            raise TypeError('next_node must be a Node Object')
        self.next_node = value


class SinglyLinkedList:
    def __init__(self):
        head = Node(0, None)

    def sorted_insert(self, value):
        new_node = Node(value, None)
