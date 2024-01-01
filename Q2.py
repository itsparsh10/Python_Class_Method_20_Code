#WAP to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")

stack = Stack()

stack.push(5)
stack.push("Hello")
stack.push(True)
stack.pop()
stack.pop()
stack.pop()
stack.pop() 
