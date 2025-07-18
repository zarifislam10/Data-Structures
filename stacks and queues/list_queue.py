class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def enqueue(self, element: str) -> None:
        """Places an element at the end of the queue."""
        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def dequeue(self) -> str:
        """Removes and returns the element at the front of the queue.
        Returns None if queue is empty."""
        if self.is_empty():
            return None
        result = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return result
    
    def front(self) -> str:
        """Returns but does not remove the element at the front of the queue.
        Returns None if queue is empty."""
        if self.is_empty():
            return None
        return self.head.data
    
    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise."""
        return self._size == 0
    
    def size(self) -> int:
        """Returns the number of elements in the queue."""
        return self._size 