class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(curr):
    if curr is None:
        return
    print(curr.val, end=' ')  # Print current node's value
    preorder(curr.left)       # Traverse left subtree
    preorder(curr.right)      # Traverse right subtree

def inorder(curr):
    if curr is None:
        return
    inorder(curr.left)        # Traverse left subtree
    print(curr.val, end=' ')  # Print current node's value
    inorder(curr.right)       # Traverse right subtree

def postorder(curr):
    if curr is None:
        return
    postorder(curr.left)      # Traverse left subtree
    postorder(curr.right)     # Traverse right subtree
    print(curr.val, end=' ')  # Print current node's value

# Example usage with the tree from the image
if __name__ == "__main__":
    # Creating the tree from the image
    # The tree structure appears to be:
    #       A
    #     /   \
    #    B     C
    #   / \     \
    #  D   E     I
    #     / \   /
    #    F   G J
    #       /
    #      H

    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.left.right.left = Node('F')
    root.left.right.right = Node('G')
    root.left.right.right.left = Node('H')
    root.right.right = Node('I')
    root.right.right.left = Node('J')

    print("Preorder traversal:", end=' ')
    preorder(root)
    print("\nInorder traversal:", end=' ')
    inorder(root)
    print("\nPostorder traversal:", end=' ')
    postorder(root)
    print() 