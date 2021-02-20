# Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_minimal_BST(array):
    return create_subtree(array, 0, len(array) - 1)

# time: O(n), space: O(n)
def create_subtree(array, start, end):
    # use middle of array as root, then subdivide array for each branch

    if end < start:
        return None

    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = create_subtree(array, start, mid - 1)
    node.right = create_subtree(array, mid + 1, end)
    return node

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=' ')
        inorder_traversal(node.right)

minimal_bst = create_minimal_BST([1, 2, 3, 4, 5])
inorder_traversal(minimal_bst)
