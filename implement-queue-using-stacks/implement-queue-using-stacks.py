class MyQueue:
    # O(n) push
    # O(1) pop
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            
        self.stack2.append(x)
        
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            
    def pop(self) -> int:
        val = self.stack2.pop()
        return val
    
    def peek(self) -> int:
        return self.stack2[-1]

    def empty(self) -> bool:
        if self.stack2:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()