from collections import deque

class ArrayQueue:
    CAPACITY = 5
    
    def __init__(self):
        self.queue = deque(maxlen=self.CAPACITY)
        self._size = 0
    
    def enqueue(self, element: str) -> None:
        """Places an element at the end of the queue."""
        if self.size() == self.CAPACITY:
            raise IllegalStateException("Queue is FULL.")
        self.queue.append(element)
        self._size += 1
    
    def dequeue(self) -> str:
        """Removes and returns the element at the front of the queue.
        Returns None if queue is empty."""
        if self.is_empty():
            return None
        self._size -= 1
        return self.queue.popleft()
    
    def front(self) -> str:
        """Returns but does not remove the element at the front of the queue.
        Returns None if queue is empty."""
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise."""
        return self._size == 0
    
    def size(self) -> int:
        """Returns the number of elements in the queue."""
        return self._size

class IllegalStateException(Exception):
    pass 