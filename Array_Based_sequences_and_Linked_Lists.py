#Thomas Cubstead
#Algorithm_Runtime_Project
#Main
#10/23/25
#This program uses stack classes to evaluate postfix expressions and convert infix expressions to postfix expressions 
#using both array-based sequences and linked lists.


#stack.py 
class Stack:
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

#evaluates postfix expressions by using a stack
class PostfixEval:
    
    def __init__(self):
        self.stack = Stack()
    
    def evaluate(self, expression):
        self.stack.clear()
        tokens = expression.split()
        
        for token in tokens:
            if self._is_operand(token):
                # Push operand onto stack
                self.stack.push(float(token))
            elif self._is_operator(token):
                # Pop two operands, apply operator, push result
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = self._apply_operator(operand1, operand2, token)
                self.stack.push(result)
        
        # Final result is the only item left on stack
        return self.stack.pop()
    
    def _is_operand(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False
    
    def _is_operator(self, token):
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
            raise ValueError(f"Unknown operator: {operator}")

#class to convert infix expressions to postfix expressions
class InfixConverter:
    def __init__(self):
        self.stack = Stack()
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
        return token.isalnum()

    def _is_operator(self, token):
        return token in self.precedence

    def _has_precedence(self, op1, op2):
        return self.precedence.get(op1, 0) >= self.precedence.get(op2, 0)

        
def main():
    # Test Data for Postfix Evaluator
    postfix = ["5 3 +", "8 2 - 3 +", "5 3 8 * +", "6 2 / 3 +", 
               "5 8 + 3 -", "5 3 + 8 *", "8 2 3 * + 6 -", 
               "5 3 8 * + 2 /", "8 2 + 3 6 * -", "5 3 + 8 2 / -"]
    
    # Test Data for Infix Converter
    infix = ["A + B", "A + B * C", "( A + B ) * C", "A * B + C / D", 
             "( A + B ) * ( C - D )", "A + B * C - D / E", 
             "A * ( B + C ) / D", "( A + B * C ) / ( D - E )", 
             "A + ( B - C ) * D", "( A + B * ( C - D ) ) / E"]

   # Test Postfix Evaluator
    print("----- Postfix Evaluator -----")
    evaluator = PostfixEval()

    for expr in postfix:
        result = evaluator.evaluate(expr)
        # Format result: if it's a whole number, show as int, otherwise as float
        if result == int(result):
            print(f"[{expr}] = {int(result)}")
        else:
            print(f"[{expr}] = {result}")

    print("\n----- Infix to Postfix Converter -----")
    converter = InfixConverter()

    for expr in infix:
        result = converter.convert(expr)
        print(f"[{expr}] -> [{result}]")

if __name__ == "__main__":
    main()