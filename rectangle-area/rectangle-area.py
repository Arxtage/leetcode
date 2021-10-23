class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # O(1)
        # sum of areas minus intersection
        intersetion_x = (min(ax2, bx2) - max(ax1, bx1))
        intersection_y = (min(ay2, by2) - max(ay1, by1))

        if intersetion_x > 0 and intersection_y > 0:
            return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - intersetion_x * intersection_y
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)