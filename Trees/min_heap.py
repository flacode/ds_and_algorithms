class MinHeap:

    """
        >>> h.insert(8)
        >>> h.insert(7)
        >>> h.insert(6)
        >>> print(h.heap)
        [6, 8, 7]
        >>> h.pop()
        6
        >>> print(h.heap)
        [7, 8]
    """

    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return int((i - 1) / 2)

    def get_left_child(self, i):
        return 2 * i + 1

    def get_right_child(self, i):
        return 2 * i + 2

    def swap(self, index_1, index_2):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    def insert(self, key):
        self.heap.append(key)
        # heapify the last index containing the item that has just been added
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, key_index):
        parent = self.get_parent(key_index)
        if parent >= 0:
            # check if parent is greater than one of the children
            if self.heap[parent] > self.heap[key_index]:
                self.swap(parent, key_index)
                self.heapify_up(parent)

    def pop(self):
        last_index = len(self.heap) - 1
        self.swap(last_index, 0)
        deleted_value = self.heap.pop()
        self.heapify_down(0)
        return deleted_value

    def heapify_down(self, key_index):
        left_child = self.get_left_child(key_index)
        right_child = self.get_right_child(key_index)

        min_child_index = -1
        if left_child < len(self.heap):
            if right_child < len(self.heap):
                if self.heap[right_child] < self.heap[left_child]:
                    min_child_index = right_child
            min_child_index = left_child

        if min_child_index == -1:
            return

        if self.heap[key_index] > self.heap[min_child_index]:
            self.swap(key_index, min_child_index)
            heapify_down(key_index)


if __name__ == "__main__":
    import doctest
    doctest.testmod(
        extraglobs={'h': MinHeap()}
    )
