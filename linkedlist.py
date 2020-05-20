# This is the core module of the CLI
# Here is where the linked list structure is built


class Node:
    data = None
    next_node = None

    def __init__(self, data: int):
        self.data = data


class LinkedList:
    head = None
    current = None
    prev = None
    counter = 0
    datatype = None

    def __init__(self, datatype):
        self.datatype = datatype

    def __str__(self):
        nodes = []
        while self.current != None:
            nodes.append(self.current.data)
            self.current = self.current.next_node
        self.current = self.head
        return nodes

    def __len__(self):
        if self.current != None:
            self.counter = self.counter + 1
            self.current = self.current.next_node
            return self.__len__()

        count = self.counter

        self.counter = 0
        self.current = self.head

        return count

    def __getitem__(self, index: int = 0):
        if self.head == None:
            raise IndexError

        if self.counter < index and self.current.next_node == None:
            self.counter = 0
            self.current = self.head
            raise IndexError

        if self.counter < index:
            self.current = self.current.next_node
            self.counter = self.counter + 1
            return self.__getitem__(index)

        data = self.current.data

        self.current = self.head
        self.counter = 0

        return data

    def foreach(self, func):
        while self.current != None:
            func(self.current.data)
            self.current = self.current.next_node

        self.current = self.head

    def append(self, **data):
        if self.head == None:
            self.head = Node(self.datatype(**data))
            self.current = self.head
            return

        if self.current.next_node != None:
            self.current = self.current.next_node
            return self.append(**data)

        self.current.next_node = Node(self.datatype(**data))

        self.current = self.head

    def insert(self, index: int = 0, **data):
        if index == 0:
            new_node = Node(self.datatype(**data))
            new_node.next_node = self.head
            self.head = new_node
            self.current = self.head
            return

        if index != 0 and self.head == None:
            raise IndexError

        if self.counter < index and self.current == None:
            self.prev = None
            self.counter = 0
            self.current = self.head
            raise IndexError

        if self.counter < index:
            self.prev = self.current
            self.current = self.current.next_node
            self.counter = self.counter + 1
            return self.insert(index, **data)

        new_node = Node(self.datatype(**data))
        new_node.next_node = self.current
        self.prev.next_node = new_node

        self.current = self.head
        self.prev = None
        self.counter = 0

    def remove(self, index: int = 0):
        if self.head == None:
            raise IndexError

        if index == 0:
            self.head = self.head.next_node
            self.current = self.head
            return

        if self.counter < index and self.current == None:
            self.prev = None
            self.current = self.head
            self.counter = 0
            raise IndexError

        if self.counter < index:
            self.prev = self.current
            self.current = self.current.next_node
            self.counter = self.counter + 1
            return self.remove(index)

        self.prev.next_node = self.current.next_node

        self.prev = None
        self.current = self.head
        self.counter = 0

    def pop(self):
        if self.head == None or self.head.next_node == None:
            self.head = None
            self.current = None
            return

        if self.current.next_node != None:
            self.prev = self.current
            self.current = self.current.next_node
            return self.pop()

        self.prev.next_node = None

        self.current = self.head
        self.prev = None
