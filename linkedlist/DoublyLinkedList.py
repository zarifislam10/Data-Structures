    class DoublyLinkedList:
        class Node:
            def __init__(self, data):
                self.data = data
                self.prev = None
                self.next = None

        def __init__(self):
            self.dummy_head = self.Node(None)
            self.tail = self.dummy_head
            self.length = 0

        def insert_first(self, data):
            node = self.Node(data)
            node.next = self.dummy_head.next
            if self.dummy_head.next is not None:
                self.dummy_head.next.prev = node
            node.prev = self.dummy_head
            self.dummy_head.next = node
            if self.length == 0:
                self.tail = node
            self.length += 1

        def insert_last(self, data):
            node = self.Node(data)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1

        def insert_at_position(self, data, pos):
            if pos == 0:
                self.insert_first(data)
            elif pos >= self.length:
                self.insert_last(data)
            else:
                node = self.Node(data)
                curr = self.dummy_head
                for _ in range(pos):
                    curr = curr.next
                
                node.next = curr.next
                node.prev = curr
                curr.next.prev = node
                curr.next = node
                self.length += 1

        def remove_first(self):
            if self.length == 0:
                return
            
            if self.length == 1:
                self.dummy_head.next = None
                self.tail = self.dummy_head
            else:
                self.dummy_head.next = self.dummy_head.next.next
                self.dummy_head.next.prev = self.dummy_head
            self.length -= 1

        def remove_last(self):
            if self.length == 0:
                return
            
            if self.length == 1:
                self.dummy_head.next = None
                self.tail = self.dummy_head
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.length -= 1

        def remove_at_position(self, pos):
            if self.length == 0 or pos >= self.length:
                return
            elif pos == 0:
                self.remove_first()
            elif pos == self.length - 1:
                self.remove_last()
            else:
                curr = self.dummy_head
                for _ in range(pos):
                    curr = curr.next
                
                curr.next.next.prev = curr
                curr.next = curr.next.next
                self.length -= 1

        def is_present(self, node):
            curr = self.dummy_head.next
            while curr is not None:
                if curr == node:
                    return True
                curr = curr.next
            return False

        def is_empty(self):
            return self.length == 0

        def get_first(self):
            return self.dummy_head.next

        def get_last(self):
            return self.tail

        def get_length(self):
            return self.length

        def to_array(self):
            result = []
            curr = self.dummy_head.next
            while curr is not None:
                result.append(curr.data)
                curr = curr.next
            return result

        def to_array_inverse(self):
            result = []
            curr = self.tail
            while curr != self.dummy_head:
                result.append(curr.data)
                curr = curr.prev
            return result 