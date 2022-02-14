# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    node_max_right = root.value
    node_max_left = root.value
    if root.left_child is not None:
        node_max_right = max(root.left_child.value, greatest_node(root.left_child))

    if root.right_child is not None:
        node_max_left = max(root.right_child.value, greatest_node(root.right_child))

    return max(node_max_left, node_max_right)

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))