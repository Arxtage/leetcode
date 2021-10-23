class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # O(n)
        hashmap = collections.Counter(moves)
        return True if (hashmap['U'] == hashmap['D']) and (hashmap['L'] == hashmap['R']) else False