class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        popped_node = self.top
        self.top = self.top.next
        self.length -= 1
        return popped_node.value

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.length == 0