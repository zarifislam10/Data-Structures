class AVLNode:
    def __init__(self, data=0):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.left_height = -1
        self.right_height = -1
        self.height = 0
    
    # Getters for troubleshooting
    def get_parent_data(self):
        if self.parent is None:
            return -1
        return self.parent.data
    
    def get_height(self):
        return self.height
    
    def get_left_height(self):
        return self.left_height
    
    def get_right_height(self):
        return self.right_height
    
    def set_data(self, n):
        self.data = n 