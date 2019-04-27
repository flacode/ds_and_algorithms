# from __future__ import annotations


class Node:
    """
        >>> node = Node("test_node")
        >>> node.has_value("test_node")
        True
        >>> node.has_value("test_nodes")
        False
    """

    def __init__(self, value: str, nextNode: "Node" = None) -> None:
        self.value = value
        self.next = nextNode

    def has_value(self, value: str) -> str:
        return self.value == value

    def __str__(self) -> str:
        return self.value


class LinkedList:
    """
        >>> linked_list._is_empty()
        True

        >>> linked_list.remove_from_front()
        'Can not delete item from an empty linked list'

        >>> linked_list.remove_specific_node("del_node")
        'Can not delete node from empty list'

        >>> n1 = Node("test_node_1")
        >>> linked_list.add_to_front(n1)
        >>> linked_list._is_empty()
        False
        >>> linked_list.print_list()
        'HEAD -> test_node_1 -> None'


        >>> n2 = Node("test_node_2")
        >>> linked_list.add_to_front(n2)
        >>> linked_list.size
        2
        >>> linked_list.print_list()
        'HEAD -> test_node_2 -> test_node_1 -> None'

        >>> linked_list.remove_from_front()
        'test_node_2'
        >>> linked_list.size
        1
        >>> linked_list.print_list()
        'HEAD -> test_node_1 -> None'

        >>> linked_list.remove_from_front()
        'test_node_1'
        >>> linked_list.size
        0
        >>> linked_list.print_list()
        'Linked list is empty'

        >>> n3 = Node("test_node_1")
        >>> linked_list2.add_to_end(n3)
        >>> linked_list2.print_list()
        'HEAD -> test_node_1 -> None'

        >>> n4 = Node("test_node_2")
        >>> linked_list2.add_to_end(n4)
        >>> linked_list2.size
        2
        >>> linked_list2.print_list()
        'HEAD -> test_node_1 -> test_node_2 -> None'

        >>> linked_list2.remove_specific_node("test_node_1").value
        'test_node_1'
        >>> linked_list2.size
        1
        >>> linked_list2.print_list()
        'HEAD -> test_node_2 -> None'

        >>> linked_list2.remove_specific_node("test_node_3")
        'Node not found'
    """

    def __init__(self) -> None:
        self.head = None
        self.size = 0
        self.tail = None  # improvement

    def _is_empty(self) -> bool:
        return self.size == 0

    def add_to_front(self, node: Node) -> None:
        # set the tail and head to the first node in the list
        if self._is_empty():
            self.tail = node

        node.next = self.head
        self.head = node
        self.size += 1

    def print_list(self) -> str:
        if self._is_empty():
            return "Linked list is empty"
        current = self.head
        slist = "HEAD"
        while current is not None:
            slist += " -> {}".format(str(current))
            current = current.next
        return slist + " -> None"

    def remove_from_front(self) -> str:
        if self._is_empty():
            return "Can not delete item from an empty linked list"
        node_to_delete = self.head
        self.head = self.head.next
        node_to_delete.next = None
        self.size -= 1

        # if it was the first node, set tail to empty
        if self._is_empty():
            self.tail = None

        return node_to_delete.value

    def add_to_end(self, node: Node) -> None:
        # if it is the first node, set head to that node also
        if self._is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def find_mid(self) -> Node:
        # using the fast runner and slow runner algorithm
        fast_runner = self.head
        slow_runner = self.head
        tick = False

        while fast_runner is not None:
            if tick:
                slow_runner = slow_runner.next
            tick = not tick
            fast_runner = fast_runner.next
        return slow_runner

    def remove_specific_node(self, node: str):
        node_to_remove = None
        if self._is_empty():
            return "Can not delete node from empty list"

        # check if it is the only node
        if self.head.has_value(node) and self.tail.has_value(node):
            node_to_remove = self.head
            self.head = None
            self.tail = None

        # check if it is the first node
        elif self.head.has_value(node):
            node_to_remove = self.head
            self.head = node_to_remove.next

        else:
            current = self.head
            prev = None
            while current is not None:
                if current.has_value(node):
                    node_to_remove = current
                    prev.next = current.next
                prev = current
                current = current.next

        if node_to_remove:
            node_to_remove.next = None
            self.size -= 1
            return node_to_remove
        return "Node not found"


if __name__ == "__main__":
    import doctest
    doctest.testmod(
        extraglobs={'linked_list': LinkedList(), 'linked_list2': LinkedList()})
