class StackException(Exception):
    pass


class LinkedListStack:
    """
    >>> stack.peek()
    Traceback (most recent call last):
    StackException: Stack is empty

    >>> stack.pop()
    Traceback (most recent call last):
    StackException: Stack is empty

    >>> stack.push('Mon')
    >>> len(stack)
    1

    >>> stack.push('Tue')
    >>> stack.peek().value
    'Tue'
    >>> len(stack)
    2

    >>> stack.pop().value
    'Tue'
    >>> len(stack)
    1



    """

    class _Node:
        def __init__(self, value: str, nextNode: "_Node" = None) -> None:
            self.value = value
            self.nextNode = nextNode

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def _is_empty(self):
        return self.size == 0

    def push(self, element):
        new_element = self._Node(element)
        new_element.nextNode = self.head
        self.head = new_element
        self.size += 1

    def pop(self):
        if self._is_empty():
            raise StackException("Stack is empty")
        element_to_delete = self.head
        self.head = element_to_delete.nextNode
        element_to_delete.nextNode = None
        self.size -= 1
        return element_to_delete

    def peek(self):
        if self._is_empty():
            raise StackException("Stack is empty")
        return self.head


if __name__ == "__main__":
    import doctest
    doctest.testmod(
        extraglobs={'stack': LinkedListStack()})
