class Solution:
    def isHappy(self, n: int) -> bool:
        # O(logn)
        history = set()
        while True:
            sm = sum(int(i)**2 for i in list(str(n)))
            if sm == 1:
                return True
            elif sm in history:
                return False
            history.add(sm)
            n = int(sm)
            