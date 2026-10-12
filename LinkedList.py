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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node
        return self

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        return self

    def find_by_index(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index != index:
            current_node = current_node.next_node
            current_index += 1
        if current_node is None:
            raise NoneException()
        return current_node.value


    def find_by_value(self, value):
        current_node = self.head
        current_index = 0
        while current_node is not None and current_node.value != value:
            current_node = current_node.next_node
            current_index += 1
        if current_node is None:
            raise NoneException()
        return current_index

    def delete_by_index(self, index):
        if index == 0:
            self.head = self.head.next_node
        current_node = self.head
        current_index = 0
        previous_node = None
        while current_node is not None and current_index != index:
            previous_node = current_node
            current_node = current_node.next_node
            current_index += 1
        if current_node is None:
            raise NoneException()
        previous_node.next_node = current_node.next_node

    def delete_by_value(self, value):
        current_node = self.head
        current_index = 0
        previous_node = None
        while current_node is not None and current_node.value != value :
            previous_node = current_node
            current_node = current_node.next_node
            current_index += 1
        if current_node is None:
            raise NoneException()
        previous_node.next_node = current_node.next_node

    def update(self, index, new_value):
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index != index:
            current_node = current_node.next_node
            current_index += 1
        if current_node is None:
            raise NoneException()
        current_node.value = new_value


linked_list = LinkedList()
linked_list.prepend(1)
print(linked_list)
linked_list.append(5)
print(linked_list)
linked_list.append(10)
print(linked_list.find_by_index(2))
print(linked_list.find_by_value(1))
linked_list.update(0, 3)
print(linked_list)
linked_list.append(4).prepend(6)
print(linked_list)
linked_list.delete_by_index(2)
print(linked_list)

linked_list.delete_by_value(3)
print(linked_list)







    