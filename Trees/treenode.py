class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def insert(self, value):
        # ignore duplicate values
        if value == self.data:
            return

        # if value is less than the value of the node, insert to the left child or find the first empty left child
        if value < self.data:
            if self.left_child:
                self.left_child.insert(value)
            else:
                self.left_child = self.__class__(value)

        # if value is greater than the value of the node, insert to the right child or find the first empty right child
        if value > self.data:
            if self.right_child:
                self.right_child.insert(value)
            else:
                self.right_child = self.__class__(value)

    def traverse_inorder(self):
        # we print the left_child -> root -> right child

        if self.left_child:
            self.left_child.traverse_inorder()

        print(self.data, end=" ")

        if self.right_child:
            self.right_child.traverse_inorder()

    def traverse_pre_order(self):
        # we print the root -> left_child -> right child
        print(self.data, end=" ")

        if self.left_child:
            self.left_child.traverse_pre_order()

        if self.right_child:
            self.right_child.traverse_pre_order()

    def traverse_post_order(self):
        # we print the left_child -> > right child -> root

        if self.left_child:
            self.left_child.traverse_post_order()

        if self.right_child:
            self.right_child.traverse_post_order()

        print(self.data, end=" ")

    def find_key(self, key):
        if self.data == key:
            return True

        # search left subtree
        elif key < self.data:
            if self.left_child:
                return self.left_child.find_key(key)

        else:
            if self.right_child:
                return self.right_child.find_key(key)

        return False

    def get_min(self):
        if self.left_child:
            return self.left_child.get_min()
        return self.data

    def get_max(self):
        if self.right_child:
            return self.right_child.get_max()
        return self.data
