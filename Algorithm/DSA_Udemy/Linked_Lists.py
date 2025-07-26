class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedLists:
    def __init__(self, value):
        self.Node = Node(value)
        self.head = self.Node
        self.tail = self.Node
        self.length = 1

    def append_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def traverse_list(self):
        values = []
        tmp = self.head
        while tmp is not None:
            values.append(tmp.value)
            tmp = tmp.next
        return values

    def pop_item(self):
        tmp = self.head
        pre = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return tmp

        while tmp.next is not None:
            pre = tmp
            tmp = tmp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return tmp


    def prepend_item(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        tmp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return tmp
        elif self.length == 0:
            return None
        else:
            self.head = self.head.next
            tmp.next = None
            self.length -= 1
            return tmp

    def get_value(self, index: int):
        if (index < 0) or (index > self.length):
            return None
        tmp = self.head
        for i in range(self.length):
            if i == index:
                break
            tmp = tmp.next
        return tmp

    def set_value(self, index: int, value: int):
        set_node = self.get_value(index)
        if set_node:
            set_node.value = value
            return True
        return False

    def insert_value(self, index: int, value: int)-> bool | None:
        if (index < 0) or (index > self.length):
            return None
        if (index == 0) or (self.length==0):
            status = self.prepend_item(value)
            return status
        if (index == self.length) and (self.length > 0):
            status = self.append_node(value)
            return status
        new_node = Node(value)
        before_index = self.get_value(index-1)
        after_index = self.get_value(index)
        before_index.next = new_node
        new_node.next = after_index
        self.length += 1
        return True

    def remove_value(self, index: int) -> bool | None:
        if (index < 0) or (index >= self.length):
            return None
        if index == 0:
            val = self.pop_first()
            return val
        if index == self.length:
            val = self.pop_item()
            return val
        if self.length == 0:
            return None
        left = self.get_value(index-1)
        tmp = self.get_value(index)
        right = self.get_value(index+1)
        left.next = right
        tmp.next = None
        self.length -= 1
        return tmp

    def reverse_linked_list(self):
        pass

my_linked_list = LinkedLists(1)
my_linked_list.append_node(2)
my_linked_list.append_node(3)
my_linked_list.append_node(4)
my_linked_list.append_node(5)

print('LL before remove():')
print(my_linked_list.traverse_list())

print('\n1. Removed node:')
print(my_linked_list.remove_value(2).value)
print('LL after remove() in middle:')
print(my_linked_list.traverse_list())

print('\n2. Removed node:')
print(my_linked_list.remove_value(0).value)
print('LL after remove() of first node:')
print(my_linked_list.traverse_list())

print('\n3. Removed node:')
print(my_linked_list.remove_value(2).value)
print('LL after remove() of last node:')
print(my_linked_list.traverse_list())

print('\n4. Removed node:')
remove_ops = my_linked_list.remove_value(6)
if remove_ops:
    print(remove_ops.value)
print('LL after remove() of last node:')
print(my_linked_list.traverse_list())