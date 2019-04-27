class Node:
    """
        >>> node = Node("test_node")
        >>> node.has_value("test_node")
        True
        >>> node.has_value("test_nodes")
        False
    """

    def __init__(self, value: str, nextNode: "Node" = None, prevNode: "Node" = None) -> None:
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

    def has_value(self, value: str) -> str:
        return self.value == value

    def __str__(self):
        return self.value


class LinkedList:
    """
    >>> linked_list._is_empty()
    True

    >>> linked_list.remove_from_front()
    'Can not delete item from an empty linked list'

    >>> linked_list.remove_from_end()
    'Can not delete item from an empty linked list'

    >>> n1 = Node("test_node_1")
    >>> linked_list.add_to_front(n1)
    >>> linked_list._is_empty()
    False
    >>> linked_list.print_list()
    'HEAD <=> test_node_1 -> None'


    >>> n2 = Node("test_node_2")
    >>> linked_list.add_to_front(n2)
    >>> linked_list.size
    2
    >>> linked_list.print_list()
    'HEAD <=> test_node_2 <=> test_node_1 -> None'

    >>> linked_list.remove_from_front().value
    'test_node_2'
    >>> linked_list.size
    1
    >>> linked_list.print_list()
    'HEAD <=> test_node_1 -> None'

    >>> linked_list.remove_from_front().value
    'test_node_1'
    >>> linked_list.size
    0
    >>> linked_list.print_list()
    'Linked list is empty'

    >>> n3 = Node("test_node_1")
    >>> linked_list2.add_to_tail(n3)
    >>> linked_list2.print_list()
    'HEAD <=> test_node_1 -> None'

    >>> n4 = Node("test_node_2")
    >>> linked_list2.add_to_tail(n4)
    >>> linked_list2.size
    2
    >>> linked_list2.print_list()
    'HEAD <=> test_node_1 <=> test_node_2 -> None'

    >>> linked_list2.remove_from_end().value
    'test_node_2'
    >>> linked_list2.size
    1
    >>> linked_list2.print_list()
    'HEAD <=> test_node_1 -> None'

    >>> linked_list2.remove_from_end().value
    'test_node_1'
    >>> linked_list2.size
    0
    >>> linked_list2.print_list()
    'Linked list is empty'
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None  # points to last node in the list
        self.size = 0

    def _is_empty(self):
        return self.size == 0

    def add_to_front(self, node: Node) -> None:
        if self._is_empty():  # both head and tail should point to node
            self.tail = node
        else:
            self.head.prevNode = node
            node.nextNode = self.head
        node.next = self.head
        self.head = node
        self.size += 1

    def add_to_tail(self, node: Node) -> None:
        if self._is_empty():  # both head and tail should point to node
            self.head = node
        else:
            self.tail.nextNode = node
        node.prevNode = self.tail
        self.tail = node
        self.size += 1

    def remove_from_front(self) -> Node:
        if self._is_empty():
            return "Can not delete item from an empty linked list"
        node_to_delete = self.head

        if node_to_delete.nextNode is None:  # if it is the only node in the list
            self.tail = None
        else:
            self.head.nextNode.prevNode = None
        self.head = self.head.nextNode
        node_to_delete.next = None
        self.size -= 1

        return node_to_delete

    def remove_from_end(self) -> Node:
        if self._is_empty():
            return "Can not delete item from an empty linked list"
        node_to_delete = self.tail
        if node_to_delete.prevNode is None:
            self.head = None
        else:
            node_to_delete.prevNode.nextNode = None
        self.tail = node_to_delete.prevNode
        node_to_delete.prevNode = None
        self.size -= 1
        return node_to_delete

    def print_list(self) -> str:
        if self._is_empty():
            return "Linked list is empty"
        current = self.head
        slist = "HEAD"
        while current is not None:
            slist += " <=> {}".format(str(current))
            current = current.nextNode
        return slist + " -> None"


if __name__ == "__main__":
    import doctest
    doctest.testmod(
        extraglobs={'linked_list': LinkedList(), 'linked_list2': LinkedList()})
