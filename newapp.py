class NoneException(Exception):
    pass

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        current_node = self.head
        acc = "["
        while current_node is not None:
            acc += str(current_node.value) + " "
            current_node = current_node.next_node

        acc += "]"
        return acc

    def find_by_index(self, index):
        a, b, c = self._check_node(lambda x,y: y != index)
        return b.value

    def find_by_value(self, value):
       a, b, c = self._check_node(lambda x,y: x.value != value)
       return a

    def delete_by_index(self, index):
        if index == 0:
            self.head = self.head.next_node
        a, b, c = self._check_node(lambda x,y : y != index)
        c.next_node = b.next_node

    def delete_by_value(self, value):
        a, b, c = self._check_node(lambda x,y: x.value != value)
        c.next_node = b.next_node

    def update(self, index, new_value):
        a, b, c = self._check_node(lambda x,y: x != index)
        b.value = new_value

    def _check_node(self,f):
        current_node = self.head
        current_index = 0
        previous_node = None
        while current_node is not None and not f(current_node, current_index):
            previous_node = current_node
            current_node = current_node.next_node
            current_index += 1
        if current_node is None:
            raise NoneException()
        else:
            return current_index, current_node, previous_node

