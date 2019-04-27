import os

from stack_linked_list import LinkedListStack


def reverse_file(file_name):
    # reverse contents of a file
    S = LinkedListStack()
    original = open(file_name)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(file_name, "w")
    while not S._is_empty():
        output.write(S.pop().value+'\n')
    output.close()


if __name__ == "__main__":
    file_name = os.path.join(os.path.dirname(__file__), "sample.txt")
    reverse_file(file_name)
