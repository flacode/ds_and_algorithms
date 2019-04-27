from stacks.stack_linked_list import LinkedListStack
from queues.queue_array import Queue


def is_palindrome_stacks(word):
    """
    >>> is_palindrome_stacks("madam")
    True
    >>> is_palindrome_stacks("racecar")
    True
    >>> is_palindrome_stacks("palace")
    False

    """
    S = LinkedListStack()
    word = word.lower()
    for character in word:
        S.push(character)

    reversed_word = ''
    while not S._is_empty():
        reversed_word += S.pop().value

    return word == reversed_word


def is_palindrome_stack_and_queue(word):
    """
    >>> is_palindrome_stack_and_queue("madam")
    True
    >>> is_palindrome_stack_and_queue("racecar")
    True
    >>> is_palindrome_stack_and_queue("palace")
    False

    """
    S = LinkedListStack()
    Q = Queue()
    word = word.lower()

    for character in word:
        S.push(character)
        Q.enqueue(character)

    for character in word:
        if S.pop().value != Q.dequeue():
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
