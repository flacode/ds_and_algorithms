class Queue:
    class _Node:
        def __init__(self, value: str, nextNode: "_Node" = None) -> None:
            self.value = value
            self.nextNode = nextNode

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        # add at the back of the queue since we can easilt add items at the tail
        new_node = self._Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.nextNode = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        # pop from the front, it is easier
        if self.is_empty():
            raise Exception("Queue is empty")
        node_to_dequeue = self.head
        self.head = self.head.nextNode
        node_to_dequeue.nextNode = None
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return node_to_dequeue.value
