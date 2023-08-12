class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise IndexError("La queue está vacía")
        removed_node = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return removed_node.value

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length
    

if __name__ == '__main__':
    my_queue = Queue()
    print(my_queue.is_empty())
    my_queue.enqueue('1')
    my_queue.enqueue('2')
    print(my_queue.is_empty())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.is_empty())
