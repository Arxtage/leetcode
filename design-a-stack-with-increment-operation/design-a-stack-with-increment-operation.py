class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [None] * maxSize
        self.curInd = 0
        self.maxSize = maxSize
        
    def push(self, x: int) -> None:
        if self.curInd < self.maxSize:
            self.stack[self.curInd] = x
            self.curInd += 1

    def pop(self) -> int:
        returnVal = -1
        if self.curInd == 0 :
            return returnVal
        else:
            self.curInd -= 1
            returnVal = self.stack[self.curInd]
            self.stack[self.curInd] = None
            return returnVal

    def increment(self, k: int, val: int) -> None:
        for ind in range(min(self.curInd, k)):
            self.stack[ind] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)