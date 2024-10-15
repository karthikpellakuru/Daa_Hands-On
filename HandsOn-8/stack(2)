class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [-1] * size
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item

# Example
size = int(input("Enter the size of the stack: "))
stack = Stack(size)
stack.push(1)
stack.push(2)
print(stack.pop())
