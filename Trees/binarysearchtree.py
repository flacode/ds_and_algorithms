from treenode import TreeNode


class BST:
    """
    Test insert
    >>> bst.insert_node(25)
    >>> bst.root.data
    25
    >>> bst.insert_node(20)
    >>> bst.insert_node(15)

    Test search
    >>> bst.search(2)
    False
    >>> bst.search(15)
    True

    >>> bst.maximum_value()
    25
    >>> bst.minimum_value()
    15
    >>> bst.insert_node(27)
    >>> bst.insert_node(30)
    >>> bst.insert_node(28)
    >>> bst.insert_node(26)
    >>> bst.maximum_value()
    30
    >>> bst.minimum_value()
    15

    Test delete root
    >>> bst.search(25)
    True
    >>> bst.root.data
    25
    >>> bst.delete_node(25)
    >>> bst.root.data
    26
    >>> bst.search(25)
    False

    Test delete leaf node
    >>> bst.search(15)
    True
    >>> bst.delete_node(15)
    >>> bst.search(15)
    False

    Test delete node with left child only
    >>> bst.insert_node(14)
    >>> bst.root.left_child.data
    20
    >>> bst.delete_node(20)
    >>> bst.root.left_child.data
    14

    >>> bst.insert_node(29)
    >>> bst.search(28)
    True
    >>> bst.delete_node(28)
    >>> bst.search(28)
    False
    >>> bst.delete_node(8)
    """

    def __init__(self, root=None):
        self.root = root

    def insert_node(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = TreeNode(value)

    def print_tree(self):
        if self.root:
            self.root.traverse_inorder()
            print()
        else:
            print("Tree is empty")

    def search(self, key):
        if self.root:
            return self.root.find_key(key)
        else:
            return None

    def maximum_value(self):
        if self.root:
            return self.root.get_max()

    def minimum_value(self):
        if self.root:
            return self.root.get_min()

    def delete_node(self, key):
        self.root = self._node_replacement(self.root, key)

    def _node_replacement(self, subtree_root, key):
        if subtree_root is None:
            return subtree_root

        if key < subtree_root.data:
            subtree_root.left_child = self._node_replacement(
                subtree_root.left_child, key)

        elif key > subtree_root.data:
            subtree_root.right_child = self._node_replacement(
                subtree_root.right_child, key)

        else:
            # case 1 and case 2
            if subtree_root.left_child is None:
                return subtree_root.right_child
            if subtree_root.right_child is None:
                return subtree_root.left_child

            # case 3 -> has 2 children
            # find min node on the right child
            # copy min value to the current subtree root.
            # delete the min node from the right child

            min_node = subtree_root.right_child.get_min()
            subtree_root.data = min_node
            subtree_root.right_child = self._node_replacement(
                subtree_root.right_child, min_node)

        return subtree_root


if __name__ == "__main__":
    import doctest
    doctest.testmod(
        extraglobs={'bst': BST()}
    )
