class ArrayStack:
    CAPACITY = 5
    
    def __init__(self):
        self.stack = []
        self._size = 0
    
    def push(self, element: str) -> None:
        """Places an element at the top of the stack."""
        if self.size() == self.CAPACITY:
            return
        self.stack.append(element)
        self._size += 1
    
    def pop(self) -> str:
        """Removes and returns the element at the top of the stack.
        Returns None if stack is empty."""
        if self.is_empty():
            return None
        self._size -= 1
        return self.stack.pop()
    
    def peek(self) -> str:
        """Returns but does not remove the element at the top of the stack.
        Returns None if stack is empty."""
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return self._size == 0
    
    def size(self) -> int:
        """Returns the number of elements in the stack."""
        return self._size 