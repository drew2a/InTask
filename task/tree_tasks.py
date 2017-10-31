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
    tree.left.left = Node(2)
    tree.left.right = Node(6)
    tree.left.left.left = Node(1)
    tree.left.left.right = Node(3)

    tree.right = Node(13)
    tree.right.left = Node(10)
    tree.right.right = Node(14)

    return tree


def __get_lowest_common_ancestor(target_nodes, reverse_links):
    node1 = target_nodes[0]
    node2 = target_nodes[1]

    node1_level = reverse_links[node1][1]
    node2_level = reverse_links[node2][1]
    if node1_level > node2_level:
        for i in range(node1_level - node2_level):
            node1 = reverse_links[node1][0]
    else:
        for i in range(node2_level - node1_level):
            node2 = reverse_links[node2][0]

    while node1 is not None and node2 is not None:
        if node1.data == node2.data:
            return node1.data
        node1 = reverse_links[node1][0]
        node2 = reverse_links[node2][0]

    return -1


def get_path(root, a):
    if root is None:
        return []

    if root.data == a:
        return [root.data]

    left_path = get_path(root.left, a)
    if len(left_path) != 0:
        return [root.data] + left_path

    right_path = get_path(root.right, a)
    if len(right_path) != 0:
        return [root.data] + right_path

    return []


def get_lowest_common_ancestor(root, a, b):
    if root is None:
        return -1

    path_a = get_path(root, a)
    if a == b:
        return a
    path_b = get_path(root, b)

    min_len = min(len(path_a), len(path_b))
    if min_len == 0:
        return -1

    for i in range(min_len):
        if path_a[i] != path_b[i]:
            return path_a[i - 1]

    return path_a[min_len - 1]
