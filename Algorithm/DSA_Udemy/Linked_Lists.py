class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
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
        if self.length <= 1:
            return

        # Swap the Head and Tail.
        tmp = self.head
        self.head = self.tail
        self.tail = tmp

        # Reverse the list
        before = None
        after = tmp.next
        while after is not None:
            after = tmp.next
            tmp.next = before
            before = tmp
            tmp = after

    def find_middle_node(self):
        """
        Interview Question.

        Assume that the Linked list has no length parameter.
        Find the middle of the Linked list.
        """
        fast = self.head
        slow = self.head
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        """
        Interview Question.
        Assume that the linked list has no length function.
        Find if the linked list is a circular list.
        """
        slow = self.head
        fast = self.head

        while (fast.next is not None) and (fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        """
        You are given a singly linked list that contains integer values, where some of these values may be duplicated.
        Note: this linked list class does NOT have a tail which will make this method easier to implement.
        Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
        """
        if self.head is None:
            return None

        start = 0
        runner = self.head
        elements = set()
        elements.add(runner.value)

        while runner.next is not None:
            if runner.next.value not in elements:
                elements.add(runner.next.value)
                runner = runner.next
                start += 1
            else:
                print("Duplicate found ", runner.next.value)
                self.remove_value(start+1)
        else:
            return True


def find_kth_from_end(ll: LinkedList, k: int) -> int | bool:
    """
    Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input,
    and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.
    """
    if ll.head is None:
        return None

    first = ll.head
    second = ll.head

    # Move both pointers k steps ahead.
    for _ in range(k-1):
        second = second.next
        if second is None:
            return None

    # Move both pointers one step at a time until the second pointer reaches the end of the linked list.
    while second.next:
        first = first.next
        second = second.next
    return first


my_linked_list_1 = LinkedList(1)
for x in range(2,10):
    my_linked_list_1.append_node(x)
my_linked_list_1.append_node(4)
# for x in range(2,10):
#     my_linked_list_1.append_node(x)

print(my_linked_list_1.traverse_list())

# print(find_kth_from_end(my_linked_list_1, 7).value)
my_linked_list_1.remove_duplicates()

print(my_linked_list_1.traverse_list())