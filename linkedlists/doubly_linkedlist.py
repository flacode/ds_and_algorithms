class Node:
    def __init__(self, value: str = None, prevNode: "Node" = None, nextNode: "Node" = None) -> "Node":
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

    def has_value(self, value):
        return self.value == value

    def __str__(self):
        return self.value


class DoublyLinkedList:
    """Uses empty nodes as guards at the start or end of list
       Simplifies logic of operations.

    >>> linked_list.print_list()
    'HEADER <=> TRAILER'

    >>> linked_list.remove_node("Mon")
    'Node not found'

    >>> n1 = linked_list.insert_node("Mon", linked_list.header, linked_list.trailer)
    >>> linked_list.size
    1
    >>> linked_list.print_list()
    'HEADER <=> Mon <=> TRAILER'

    >>> n2 = linked_list.insert_node("Tue", linked_list.header, n1)
    >>> linked_list.size
    2
    >>> linked_list.print_list()
    'HEADER <=> Tue <=> Mon <=> TRAILER'

    >>> n3 = linked_list.insert_node("Sun", n1, linked_list.trailer)
    >>> linked_list.size
    3
    >>> linked_list.print_list()
    'HEADER <=> Tue <=> Mon <=> Sun <=> TRAILER'

    """

    def __init__(self) -> None:
        self.header = Node()
        self.trailer = Node()
        self.header.nextNode = self.trailer
        self.trailer.prevNode = self.header
        self.size = 0

    def print_list(self) -> str:
        slist = "HEADER"
        current = self.header.nextNode
        while current is not None:
            if current.value:
                slist += " <=> {}".format(str(current))
            current = current.nextNode
        return slist + " <=> TRAILER"

    def insert_node(self, value: str, predecessor: Node, successor: Node) -> Node:
        node_to_insert = Node(value, predecessor, successor)
        predecessor.nextNode = node_to_insert
        successor.prevNode = node_to_insert
        self.size += 1
        return node_to_insert

    def remove_node(self, value: str) -> Node:
        current = self.header.nextNode
        while current is not None:
            if current.has_value(value):
                node_to_delete = current
                predecessor = node_to_delete.prevNode
                successor = node_to_delete.nextNode
                predecessor.nextNode = successor
                successor.prevNode = predecessor
                node_to_delete.prevNode = node_to_delete.nextNode = None
                self.size -= 1
                return node_to_delete
            current = current.nextNode
        return "Node not found"


if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    import doctest
    doctest.testmod(
        extraglobs={'linked_list': DoublyLinkedList(), 'linked_list2': DoublyLinkedList()})
