class TreeNode:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

    def addLeftChild(treeNode):
        self.left = treeNode

    def addRightChild(treeNode):
        self.right = treeNode

    def __repr__(self):
        return self.data

    def __eq__(self, obj):
        return isinstance(obj, Node) and obj.data == self.data


class BSTTree(object):
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
        self.data = None

    def insert_element(self, data: object) -> None:
        newNode = TreeNode(data)

        if self.root == None:
            self.root = newNode
        else:
            self._insert(self.root, newNode)

    def _insert(self, parent: TreeNode, child: TreeNode):

        if parent.data < child.data:
            if parent.right == None:
                parent.right = TreeNode
            else:
                self._insert(parent.right, child)
        else:
            if parent.left == None:
                parent.left = TreeNode
            else:
                self._insert(parent.left, child)


if __name__ == "__main__":
    tree = BSTTree()
    tree.insert_element("10")
    tree.insert_element("30")
    tree.insert_element("15")
    tree.insert_element("40")
    tree.insert_element("50")
