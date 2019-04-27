
from typing import Any


class StackException(Exception):
    pass


class ListStack:
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
    >>> stack.peek()
    'Tue'
    >>> len(stack)
    2

    >>> stack.pop()
    'Tue'
    >>> len(stack)
    1
    """

    def __init__(self) -> None:
        self.stacked_elements = []

    def __len__(self) -> int:
        return len(self.stacked_elements)

    def is_empty(self) -> bool:
        return len(self.stacked_elements) == 0

    def push(self, element: Any) -> None:
        self.stacked_elements.append(element)

    def pop(self) -> str:
        if self.is_empty():
            raise StackException("Stack is empty")
        return self.stacked_elements.pop()

    def peek(self) -> str:
        if self.is_empty():
            raise StackException("Stack is empty")
        return self.stacked_elements[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod(
        extraglobs={'stack': ListStack()})
