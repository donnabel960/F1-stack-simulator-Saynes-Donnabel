"""Stack Object"""
class Stack:
    def __init__(self, items=None):
        self.items = list(items or [])  # Copy previous values into this object.

    def push(self, value):
        self.items.append(value)  # The last element represents the top.

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

