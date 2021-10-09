class MinStack:

    def __init__(self):
        # list of lists <val, curr_min>
        self.stack = [[2**31 - 1, 2**31 - 1]] # adding max vals from beginning, not to check later if empty
        

    def push(self, val: int) -> None:
        
        if val < self.stack[-1][1]:
            self.stack.append([val, val])
        else:
            self.stack.append([val, self.stack[-1][1]])

    def pop(self) -> None:
        self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()