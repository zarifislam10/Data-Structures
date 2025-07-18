#Heap

class MinHeap:
    def __init__(self):
        self.heap = [0]  # Dummy value at index 0 for easy 1-based indexing

    def insert_min_heap(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)  # checks if the new value is smaller than its parent, and if so, it swaps up to maintain the min-heap property.

    def remove_min_heap(self):
        if self.is_empty():
            raise Exception("Heap is empty")

        if len(self.heap) == 2:
            return self.heap.pop()  # Only one real element

        res = self.heap[1]               # Save the min (root)
        self.heap[1] = self.heap.pop()   # Move last value to root and remove last
        index = 1                        # Start percolating down from the root
        
    def heapify_down(self):
        while 2 * index < len(self.heap):
            left = 2 * index
            right = 2 * index + 1
            smallest = index

    # checks if it's in bound and the left/right node is smaller than the current value
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:  
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break

        return res

    def heapify_up(self, index):
        while index > 1:
            parent = index // 2
            if self.heap[index] < self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 1

    def __str__(self):
        return str(self.heap[1:])  # Show only the real heap (skip dummy)
        
        
# ---------------------------------------------------------------------
    import heapq

class MinHeap:
    def __init__(self):
        self.heap = []  # No dummy needed

    def insert_min_heap(self, val):
        heapq.heappush(self.heap, val)

    def remove_min_heap(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)
