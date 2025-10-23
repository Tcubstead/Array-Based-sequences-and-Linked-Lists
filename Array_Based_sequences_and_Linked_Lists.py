#Thomas Cubstead
#Algorithm_Runtime_Project
#Main
#10/23/25
#This program uses stack classes to evaluate postfix expressions and convert infix expressions to postfix expressions 
#using both array-based sequences and linked lists.


#stack.py 
class stack:
    #initialize an empty stack
    def __init__(self):
        self._items = []
    #stack methods
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items) == 0

    def clear(self):
        self._items.clear()

    def __str__(self):
        return str(self._items)