class Node():
    def __init__(self, val, nxt = None, prev = None):
        self.val = val
        self.next = nxt
        self.prev = prev
        
class MyCircularDeque:
    # linked list (two ways)
    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.deque = None
        self.front = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        if not self.size:
            self.front = Node(val = value)
            self.last = self.front
        elif self.front:
            self.front.prev = Node(val = value, nxt = self.front)
            self.front = self.front.prev
            if not self.last:
                self.last = self.front.next
        elif self.last:
            self.last.prev = Node(val = value, nxt = self.last)
            self.front = self.last.prev
        self.size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        if not self.size:
            self.last = Node(val = value)
        elif self.last:
            self.last.next = Node(val = value, prev = self.last)
            self.last = self.last.next
            if not self.front:
                self.front = self.last.prev
        elif self.front:
            self.front.next = Node(val = value, prev = self.front)
            self.last = self.front.next
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if not self.size:
            return False
        if self.size == 1:
            self.last = None
            self.front = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
    
        return True
            

    def deleteLast(self) -> bool:
        if not self.size:
            return False
        if self.size == 1:
            self.last = None
            self.front = None
        else:
            self.last = self.last.prev
            self.last.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if not self.size:
            return -1
        if not self.front:
            return self.last.val
        return self.front.val
    
    def getRear(self) -> int:
        if not self.size:
            return -1
        if not self.last:
            return self.front.val
        return self.last.val
            

    def isEmpty(self) -> bool:
        return False if self.size else True

    def isFull(self) -> bool:
        return True if self.size == self.k else False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()