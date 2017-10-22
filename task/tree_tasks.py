import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        s = '{}({}, {})'.format(self.data, self.left, self.right)
        return s


class ExtendedNode:
    def __init__(self, source_node, min_value, max_value):
        self.source_node = source_node
        self.min_value = min_value
        self.max_value = max_value


def check_binary_search_tree(root):
    if root is None:
        return False

    closed = {root.data}
    opened = []
    if root.left is not None:
        opened.append(ExtendedNode(root.left, -sys.maxsize, root.data))
    if root.right is not None:
        opened.append(ExtendedNode(root.right, root.data, sys.maxsize))

    while len(opened) > 0:
        next_opened = []
        for ex_node in opened:
            source_node = ex_node.source_node
            data = source_node.data

            if not ex_node.min_value < data < ex_node.max_value or data in closed:
                return False
            closed.add(data)

            if source_node.left is not None:
                next_opened.append(ExtendedNode(source_node.left, min(data, ex_node.min_value), data))

            if source_node.right is not None:
                next_opened.append(ExtendedNode(source_node.right, data, max(data, ex_node.max_value)))

        opened = next_opened

    return True


def create_sample_tree():
    tree = Node(8)
    tree.left = Node(4)
    tree.right = Node(13)

    tree.left.left = Node(2)
    tree.left.right = Node(6)

    tree.right.left = Node(10)
    tree.right.right = Node(14)

    tree.left.left.left = Node(1)
    tree.left.left.right = Node(3)

    return tree
