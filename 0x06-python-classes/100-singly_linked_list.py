#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if not type(data) == int:
            raise TypeError('data must be an integer')
        if next_node is None or type(next_node) == Node:
            self.__data = data
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')

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
        if value is None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        self.__head = Node(value, self.__head)

    def __str__(self):
        lista = []
        while self.__head is not None:
            lista.append(self.__head.data)
            self.__head = self.__head.next_node
        lista = sorted(lista)
        str0 = ''
        if lista == []:
            return str0
        for i in range(len(lista) - 1):
            str0 = str0 + str(lista[i]) + '\n'
        str0 = str0 + str(lista[-1])
        return str0
