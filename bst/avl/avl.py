from avl_node import AVLNode

class AVL:
    def __init__(self):
        self.root = None
    
    def delete(self):
        """Erase the old tree when reading the next line"""
        self.root = None
    
    def insert(self, node):
        """Public insert method that calls the private insert method"""
        self.root = self._insert(self.root, node)
    
    def _insert(self, t, node):
        """Private insert method that handles the actual insertion and balancing"""
        if t is None:
            t = node  # insert when you reach the end (null)
        else:
            if t.data > node.data:  # go left
                t.left = self._insert(t.left, node)  # "glue the tree together"
                t.left.parent = t  # Identify the parent of the new node
                t.left_height += 1  # increase the left height of the node
                self._update_height(t)  # update the node to the new height
            elif t.data < node.data:  # go right
                t.right = self._insert(t.right, node)  # "glue the tree together"
                t.right.parent = t
                t.right_height += 1
                self._update_height(t)
        
        # Check for imbalance and perform rotations if necessary
        balance = self._get_balance(t)
        if balance == 2:  # Left heavy
            if self._get_balance(t.left) == 1:  # (2,1) case only rotate right
                t = self._right_rotate(t)
            elif self._get_balance(t.left) == -1:  # (2,-1) case rotate left then right
                t.left = self._left_rotate(t.left)
                t = self._right_rotate(t)
        elif balance == -2:  # Right heavy
            if self._get_balance(t.right) == -1:  # (-2,-1) case only rotate left
                t = self._left_rotate(t)
            elif self._get_balance(t.right) == 1:  # (-2,1) case rotate right then left
                t.right = self._right_rotate(t.right)
                t = self._left_rotate(t)
        
        return t
    
    def _right_rotate(self, t):
        """Perform a right rotation at node t"""
        temp = t.left  # make the rotation
        t.left = temp.right
        temp.right = t
        temp.parent = t.parent  # update parents
        t.parent = temp
        self._update_height(t)  # update heights
        self._update_height(temp)
        return temp
    
    def _left_rotate(self, t):
        """Perform a left rotation at node t"""
        temp = t.right  # make the rotation
        t.right = temp.left
        temp.left = t
        temp.parent = t.parent  # update parents
        t.parent = temp
        self._update_height(t)  # update heights
        self._update_height(temp)
        return temp
    
    def _get_balance(self, node):
        """Returns the balance factor of the node (left_height - right_height)"""
        return node.left_height - node.right_height
    
    def _update_height(self, node):
        """Updates the height of the node and its children"""
        # Update left height
        if node.left is not None:
            node.left_height = node.left.height
        else:
            node.left_height = -1
        
        # Update right height
        if node.right is not None:
            node.right_height = node.right.height
        else:
            node.right_height = -1
        
        # Update node height
        node.height = max(node.left_height, node.right_height) + 1
    
    def print_avl(self):
        """Public method to print the AVL tree"""
        if self.root is not None:
            self._print_avl(self.root)
    
    def _print_avl(self, node):
        """Private method to print the AVL tree using pre-order traversal"""
        if node is not None:
            print(node.data, end=' ')
            self._print_avl(node.left)
            self._print_avl(node.right) 