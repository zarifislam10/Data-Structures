from collections import deque  # For Queue implementation
from typing import Optional  # For type hints

class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, x: int) -> None:
        """Insert a new value into the BST"""
        if self.root is None:
            self.root = TreeNode(x)
        else:
            self._insert_helper(self.root, x)
    
    def _insert_helper(self, node: TreeNode, x: int) -> None:
        """Helper method for insert operation"""
        if x <= node.data:  # go left
            if node.left is None:
                node.left = TreeNode(x)
            else:
                self._insert_helper(node.left, x)
        else:  # go right
            if node.right is None:
                node.right = TreeNode(x)
            else:
                self._insert_helper(node.right, x)
    
    def search(self, x: int) -> Optional[TreeNode]:
        """Search for a value in the BST"""
        if self.root is None:
            return None
        return self._search_helper(self.root, x)
    
    def _search_helper(self, node: TreeNode, x: int) -> Optional[TreeNode]:
        """Helper method for search operation"""
        if node is None or x == node.data:
            return node
        elif x < node.data:
            return self._search_helper(node.left, x)
        else:
            return self._search_helper(node.right, x)
    
    def delete(self, x: int) -> Optional[TreeNode]:
        """Delete a value from the BST"""
        return self._delete_helper(self.root, x)
    
    def _delete_helper(self, node: TreeNode, x: int) -> Optional[TreeNode]:
        """Helper method for delete operation"""
        if node is None:
            return node
        
        if x < node.data:
            node.left = self._delete_helper(node.left, x)
        elif x > node.data:
            node.right = self._delete_helper(node.right, x)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node with two children: Get the inorder successor (smallest in right subtree)
                node.data = self._max_value(node.left)
                node.left = self._delete_helper(node.left, node.data)
        
        return node
    
    def _max_value(self, node: TreeNode) -> int:
        """Find the maximum value in a subtree"""
        if node.right is None:
            return node.data
        return self._max_value(node.right)
    
    def inorder(self) -> None:
        """Print the BST using inorder traversal (recursive)"""
        self._inorder_helper(self.root)
    
    def _inorder_helper(self, root: TreeNode) -> None:
        """Helper method for inorder traversal"""
        if root is None:
            return
        self._inorder_helper(root.left)
        print(root.data)
        self._inorder_helper(root.right)
    
    def inorder_stack(self) -> None:
        """Print the BST using inorder traversal (iterative with stack)"""
        if self.root is None:
            return
        
        stack = []
        curr = self.root
        
        while curr is not None or stack:
            # Reach the leftmost node of current node
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            # Process current node
            curr = stack.pop()
            print(curr.data)
            
            # Move to right subtree
            curr = curr.right
    
    def bfs(self) -> None:
        """Print the BST using breadth-first search"""
        if self.root is None:
            return
        
        queue = deque([self.root])
        
        while queue:
            temp = queue.popleft()
            print(temp.data)
            
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)

def main():
    # Create and test the BST
    bst = BST()
    
    # Insert some values
    bst.insert(11)
    bst.insert(0)
    bst.insert(25)
    bst.insert(3)
    bst.insert(17)
    bst.insert(100)
    bst.insert(-3)
    
    print("Inorder traversal after insertions:")
    bst.inorder()
    
    # Delete a value and show the result
    bst.delete(17)
    print("\nInorder traversal after deleting 17:")
    bst.inorder()

if __name__ == "__main__":
    main() 