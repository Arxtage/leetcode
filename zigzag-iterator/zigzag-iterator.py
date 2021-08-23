class ZigzagIterator:
    # Create a list beforehand
    def __init__(self, v1: List[int], v2: List[int]):
        L, R = 0, 0 
        self.res = []
        while L < len(v1) and R < len(v2):
            self.res.append(v1[L])
            L += 1
            self.res.append(v2[R])
            R += 1
            
        while L < len(v1):
            self.res.append(v1[L])
            L += 1
        while R < len(v2):
            self.res.append(v2[R])
            R += 1

    def next(self) -> int:
        val = self.res.pop(0)
        return val

    def hasNext(self) -> bool:
        if self.res:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())