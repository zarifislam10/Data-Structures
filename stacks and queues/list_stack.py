class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListStack:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def push(self, element: str) -> None:
        """Places an element at the top of the stack."""
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def pop(self) -> str:
        """Removes and returns the element at the top of the stack.
        Returns None if stack is empty."""
        if self.is_empty():
            return None
        result = self.head.data
        self.head = self.head.next
        self._size -= 1
        return result
    
    def peek(self) -> str:
        """Returns but does not remove the element at the top of the stack.
        Returns None if stack is empty."""
        if self.is_empty():
            return None
        return self.head.data
    
    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return self._size == 0
    
    def size(self) -> int:
        """Returns the number of elements in the stack."""
        return self._size 