class MaxHeap:
    """
        >>> h.insert(8)
        >>> h.insert(7)
        >>> h.insert(6)
        >>> print(h.heap)
        [8, 7, 6]
        >>> h.pop()
        8
        >>> print(h.heap)
        [7, 6]
    """

    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return int((i - 1) / 2)

    def get_left_child(self, i):
        return (2 * i) + 1

    def get_right_child(self, i):
        return (2 * i) + 2

    def swap(self, index_1, index_2):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    def insert(self, key):
        self.heap.append(key)
        # heapify using the last index in heap
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        parent = self.get_parent(i)  # index of parent
        if parent >= 0 and self.heap[parent] < self.heap[i]:
            self.swap(i, parent)
            self.heapify_up(parent)

    def pop(self):
        # replaces the largest item
        if len(self.heap) == 0:
            return - 1
        last_index = len(self.heap) - 1
        # root is at position 0 ie largest item
        self.swap(0, last_index)
        root = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        left_child = self.get_left_child(i)
        right_child = self.get_right_child(i)

        # get maximum child
        max_child = -1
        if left_child < len(self.heap):
            if right_child < len(self.heap):
                if self.heap[left_child] < self.heap[right_child]:
                    max_child = right_child
            else:
                max_child = left_child

        if max_child == -1:
            return

        if self.heap[i] < self.heap[max_child]:
            self.swap(i, max_child)
            self.heapify_down(i)
        else:
            return


if __name__ == "__main__":
    import doctest
    doctest.testmod(
        extraglobs={'h': MaxHeap()}
    )
