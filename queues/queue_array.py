class Queue:
    """
    Follows FIFO implementation backed by a python list
    - Throws exception when queue is empty for peek and
        dequeue operations
    - If the number items to be queued is greater than
        the capacity, we resize the list by increasing
        its capacity by 2
    - If items deleted decreases the number of items to
        less than a quarter of the capacity of items, the
        list is resized to half its capicity.
    >>> stack._is_empty()
    True

    >>> stack.enqueue(1)
    >>> len(stack)
    1

    >>> stack.enqueue(2)
    >>> stack.enqueue(3)
    >>> stack.enqueue(4)
    >>> stack.enqueue(5)
    >>> stack.enqueue(6)
    >>> stack.enqueue(7)
    >>> len(stack)
    7
    >>> len(stack._data)
    12

    >>> stack.dequeue()
    1
    >>> len(stack)
    6
    >>> len(stack._data)
    12

    >>> stack.dequeue()
    2
    >>> stack.dequeue()
    3
    >>> stack.dequeue()
    4
    >>> stack.dequeue()
    5
    >>> len(stack)
    2
    >>> len(stack._data)
    6

    """

    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size == 0

    def resize(self, capacity):
        old_list = self._data
        self._data = [None] * capacity

        """
        Copy current front to positon 0,1,2... in the new_list ie bring all elements
        to the front of the new queue in their order
        """
        for i in range(self._size):
            self._data[i] = old_list[self._front]
            self._front = (self._front + 1) % len(old_list)
        self._front = 0

    def enqueue(self, item):
        if self._size == len(self._data):
            # resize queue
            self.resize(2*len(self._data))

        available_index = (self._front + self._size) % len(self._data)
        self._data[available_index] = item
        self._size += 1

    def dequeue(self):
        if self._is_empty():
            raise Exception("Queue is empty")

        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self.resize(len(self._data)//2)
        return item

    def peek(self):
        if self._is_empty():
            raise Exception("Queue is empty")

        return self._data[self._front]


if __name__ == "__main__":
    import doctest
    doctest.testmod(
        extraglobs={'stack': Queue(6)})
