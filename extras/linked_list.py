class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            aux = self.current
            self.current = self.current.get_next()
            return aux


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def add(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            for node in self:
                if node.next is None:
                    node.next = new_node


class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_data(self):
        return self.item
    
    def __repr__(self):
        return str(self.item)


test_list = LinkedList()
test_list.add("Pablo")
test_list.add("Carlos")
test_list.add("Francisco")
for node in test_list:
    print(node)
