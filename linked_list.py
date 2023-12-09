class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class InputError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        curr_node = self.head

        if curr_node is None:
            print('LL is empty')
            return
        while curr_node is not None:
            if curr_node.next is None:
                print(curr_node.data, end='')
            else:
                print(curr_node.data, end='->')
            curr_node = curr_node.next
        print()

    def append_left(self, data=None):
        if data is None:
            print('No data inputted')
            return

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append_right(self, data=None):
        if data is None:
            print('No data inputted')
            return

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new_node

    def insert_at(self, data=None, idx=None):
        if not isinstance(idx, int):
            print('Index type must be integer')

        if idx is None:
            idx = self.length()

        if idx < 0:
            print('Index must be greater than 0')
            return

        if idx > self.length()-1:
            print(f'Index must be lesser than max length {self.length()}')
            return

        if self.head is None or idx == 0:
            self.append_left(data)
            return

        new_node = Node(data)

        curr_node = self.head
        prev_node = curr_node

        count = 0
        while curr_node is not None:
            if count == idx:
                prev_node.next = new_node
                new_node.next = curr_node
                return
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        else:
            print('Index not found')

    def remove_node(self, data=None, all_n=False):
        if data is None:
            print('No data inputted')
            return

        if self.head is None:
            print('LL is empty')
            return

        prev_node = None
        curr_node = self.head
        found = False
        while curr_node is not None:
            if data == curr_node.data:
                if prev_node is None:
                    found = True
                    self.head = curr_node.next
                    if not all_n:
                        return
                if prev_node is not None:
                    found = True
                    prev_node.next = curr_node.next
                    if not all_n:
                        return

            prev_node = curr_node
            curr_node = curr_node.next

        if found:
            pass
        else:
            print('Element not found')

    def remove_at(self, idx=None):
        if not isinstance(idx, int):
            print('Index must be integer')

        if self.head is None:
            print('LL is empty')
            return

        node_data = self.data_at(idx)
        self.remove_node(node_data)

    def data_at(self, idx=None):
        if not isinstance(idx, int):
            print('Index must be integer')

        if self.head is None:
            print('LL is empty')
            return

        if idx < 0:
            print('Index must be greated than 0')
        if idx > self.length():
            print(f'Index must be lesser than max length of {self.length()}')

        count = 0
        curr_node = self.head
        while curr_node is not None:
            if count == idx:
                return curr_node.data

            curr_node = curr_node.next
            count += 1
        else:
            print('Index not available')

    def length(self):
        curr_node = self.head
        if curr_node is None:
            return 0

        count = 0
        while curr_node is not None:
            curr_node = curr_node.next
            count += 1

        return count


ll = LinkedList()

ll.print_linked_list()
print(ll.length())

ll.append_left(1)
ll.print_linked_list()
ll.append_left(2)
ll.print_linked_list()
ll.append_left(3)
ll.print_linked_list()

ll.append_right('x')
ll.print_linked_list()
ll.append_right('y')
ll.append_right('z')
ll.append_right('z')
ll.append_right('z')
ll.print_linked_list()

ll.print_linked_list()
print(ll.length())

ll.remove_node('z')
ll.print_linked_list()
print(ll.length())

print(ll.data_at(2))
ll.remove_at(2)
ll.print_linked_list()

ll.insert_at('x', 4)
ll.print_linked_list()
