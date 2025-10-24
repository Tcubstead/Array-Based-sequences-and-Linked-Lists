#Thomas Cubstead
#Algorithm_Runtime_Project
#singlely_Linked_Lists.py
#10/23/25
#This stores the isinglely linked list ADT file


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    class EmptyListException(Exception):
        pass

    class NodeNotFoundException(Exception):
        pass

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def build_forward_list(self, iterable):
        for item in iterable:
            self.__append(item)

    def build_backward_list(self, iterable):
        for item in iterable:
            self.__prepend(item)

    def __append(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count += 1

    def __prepend(self, value):
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        if self.__tail is None:
            self.__tail = new_node
        self.__count += 1

    def insert_after(self, after_value, new_value):
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        current = self.__head
        while current and current.data != after_value:
            current = current.next
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
        if current == self.__tail:  
            self.__tail = new_node  
        self.__count += 1

    def remove(self, value):
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        current = self.__head
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()
        if previous is None:
            self.__head = current.next  
        else:
            previous.next = current.next  
        if current == self.__tail:
            self.__tail = previous  
        self.__count -= 1

    def remove_all(self, value):
        """Remove all nodes with the specified value"""
        if self.__head is None:
            return
        
        while self.__head is not None and self.__head.data == value:
            self.__head = self.__head.next
            self.__count -= 1
        
        if self.__head is None:
            self.__tail = None
            return
        
        current = self.__head
        while current.next is not None:
            if current.next.data == value:
                if current.next == self.__tail:
                    self.__tail = current
                current.next = current.next.next
                self.__count -= 1
            else:
                current = current.next

    def display(self):
        current = self.__head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Head -> " + " -> ".join(elements) + " -> None")

    def display_reverse(self):
        def _reverse_recursive(node):
            return _reverse_recursive(node.next) + [node.data] if node else []
        print("None <- " + " <- ".join(map(str, _reverse_recursive(self.__head))) + " <- Head")

    def display_reverse_nr(self):
        """Display the list in reverse order without recursion (using stack)"""
        if self.__head is None:
            print("None <- Head")
            return
        
        stack = []
        current = self.__head
        
        while current is not None:
            stack.append(current.data)
            current = current.next
        
        result = "None"
        while stack:
            result += f" <- {stack.pop()}"
        result += " <- Head"
        print(result)

    def __iter__(self):
        current = self.__head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.__count