import os

from stack_linked_list import LinkedListStack


def match_parentheses(string_characters):
    """
    >>> match_parentheses("[(match)]")
    True
    >>> match_parentheses("[(match}]")
    False
    >>> match_parentheses("[(ma(t)ch)]")
    True
    >>> match_parentheses("[(mat(ch)]")
    False
    """
    left_parenteses = "({["
    right_parenteses = ")}]"
    S = LinkedListStack()

    for character in string_characters:
        if character in left_parenteses:
            S.push(character)
        elif character in right_parenteses:
            if S._is_empty():
                return False
            if right_parenteses.index(character) != left_parenteses.index(S.pop().value):
                return False
    return S._is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
