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

#class to convert infix expressions to postfix expressions
class InfixConverter:
    def __init__(self):
        self.stack = stack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '/': 2}

    def convert(self, expression):
        self.stack.clear()
        postfix = []
        tokens = expression.split()

        for token in tokens:
            if self._is_operand(token):
                postfix.append(token)
            elif token == '(':
                self.stack.push(token)
            elif token ==')':
                while not self.stack.is_empty() and self.stack.peek() != '(':
                    postfix.append(self.stack.pop())
                self.stack.pop()
            elif self._is_operator(token):
                while (not self.stack.is_empty() and
                       self.stack.peek() != '(' and
                       self._has_precedence(self.stack.peek(), token)):
                    postfix.append(self.stack.pop())
                self.stack.push(token)

        while not self.stack.is_empty():
            postfix.append(self.stack.pop())

        return ' '.join(postfix)

    def _is_operand(self, token):
        return token.isalum()

    def _is_operator(self, token):
        return token in self.precedence

    def _has_precedence(self, op1, op2):
        return self.precedence(op1, 0) >= self.precednce.get(op2, 0)

#evaluates postfix expressions by using a stack
class PostfixEval:
    def __init__(self):
        self.stack = stack()

    def evaluate(self, expression):
        self.stack.clear()
        tokens = expression.split()

        for token in tokens:
            if self._is_operator(token):
                self.stack.push(float(token))
            elif self._is_operator(token):
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = self._apply_operator(operand1, operand2, token)
                self.stack.push(result)

        return self.stack.pop()

    def _is_operator(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    def _apply_operator(self, token):
        return token in ['+', '-', '*', '/']

    def _apply_operator(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        else:
            raise ValueError(f"Unkown operator: {operator}")
        