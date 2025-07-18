from tree_node import TreeNode
from tree_traversal import TreeTraversal
from tree_operations import TreeOperations

class BST:
    """
    Binary Search Tree implementation.
    Properties:
    - All values in left subtree are less than or equal to root
    - All values in right subtree are greater than root
    - Both left and right subtrees are also BSTs
    """
    def __init__(self):
        self.root = None
        self.size = 0  # Keep track of number of nodes
    
    def insert(self, value):
        """
        Insert a new value into the BST.
        Example:
            bst = BST()
            bst.insert(5)  # Creates root node with value 5
            bst.insert(3)  # Creates left child of root
            bst.insert(7)  # Creates right child of root
        """
        if self.root is None:
            self.root = TreeNode(value)
            self.size += 1
        else:
            self._insert_helper(self.root, value)
    
    def _insert_helper(self, node, value):
        """
        Helper method for insert.
        Recursively finds the correct position to insert the new value.
        """
        if value <= node.data:  # Go left if value is less than or equal
            if node.left is None:
                node.left = TreeNode(value)
                self.size += 1
            else:
                self._insert_helper(node.left, value)
        else:  # Go right if value is greater
            if node.right is None:
                node.right = TreeNode(value)
                self.size += 1
            else:
                self._insert_helper(node.right, value)
    
    def search(self, value):
        """
        Search for a value in the BST.
        Returns the node containing the value or None if not found.
        Example:
            bst = BST()
            bst.insert(5)
            bst.insert(3)
            node = bst.search(3)  # Returns node with value 3
        """
        if self.root is None:
            return None
        return self._search_helper(self.root, value)
    
    def _search_helper(self, node, value):
        """
        Helper method for search.
        Recursively searches for the value in the tree.
        """
        if node is None or value == node.data:
            return node
        elif value < node.data:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)
    
    def delete(self, value):
        """
        Delete a value from the BST.
        Example:
            bst = BST()
            bst.insert(5)
            bst.insert(3)
            bst.delete(3)  # Removes node with value 3
        """
        self.root = self._delete_helper(self.root, value)
        self.size -= 1  # Decrease size after deletion
    
    def _delete_helper(self, node, value):
        """
        Helper method for delete.
        Handles three cases:
        1. Node has no children
        2. Node has one child
        3. Node has two children
        """
        if node is None:
            return node
        
        if value < node.data:
            node.left = self._delete_helper(node.left, value)
        elif value > node.data:
            node.right = self._delete_helper(node.right, value)
        else:
            # Case 1 & 2: Node has no children or one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: Node has two children
            else:
                # Find the maximum value in left subtree
                node.data = self._max_value(node.left)
                # Delete the node with that value
                node.left = self._delete_helper(node.left, node.data)
        return node
    
    def _max_value(self, node):
        """
        Find the maximum value in a subtree.
        Used in delete operation.
        """
        if node.right is None:
            return node.data
        return self._max_value(node.right)

    # Delegate to TreeTraversal class
    def inorder(self):
        TreeTraversal.inorder(self.root)
    
    def bfs(self):
        TreeTraversal.bfs(self.root)

    # Delegate to TreeOperations class
    def is_root(self, node):
        return TreeOperations.is_root(node, self.root)

    def is_external(self, node):
        return TreeOperations.is_external(node)

    def is_internal(self, node):
        return TreeOperations.is_internal(node)

    def node_depth(self, node):
        return TreeOperations.node_depth(self.root, node)

# =============================================
# From Main.java
# =============================================
# Example usage:
if __name__ == "__main__":
    # Create a new BST
    bst = BST()
    
    # Insert some values
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        bst.insert(value)
    
    print("Inorder traversal (sorted order):")
    bst.inorder()  # Should print: 1 3 4 5 6 7 8
    
    print("\nBreadth-first traversal (level by level):")
    bst.bfs()  # Should print: 5 3 7 1 4 6 8
    
    # Search for a value
    search_value = 4
    result = bst.search(search_value)
    print(f"\nSearching for {search_value}:", "Found" if result else "Not found")
    
    # Delete a value
    delete_value = 3
    print(f"\nDeleting {delete_value}")
    bst.delete(delete_value)
    
    print("Inorder traversal after deletion:")
    bst.inorder()  # Should print: 1 4 5 6 7 8

    # Additional tree operations
    print("\nTree properties:")
    print(f"Tree height: {bst.tree_height()}")
    print(f"Tree size: {bst.get_size()}")
    print(f"Is root node 5?: {bst.is_root(bst.root)}")
    print(f"Is node 4 external?: {bst.is_external(bst.search(4))}")
    print(f"Is node 5 internal?: {bst.is_internal(bst.root)}")
    print(f"Depth of node 4: {bst.node_depth(bst.search(4))}") 