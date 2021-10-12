class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # O(n)
        
        stack = []
        maxim = 0
        for index, height in enumerate(heights):
            index_pop = None
            while stack and stack[-1][1] > height:
                index_pop, height_pop = stack.pop()
                if height_pop * (index - index_pop) > maxim:
                    maxim = height_pop * (index - index_pop)
            
            # extend backwards
            if index_pop != None:
                stack.append([index_pop, height])
            else:
                stack.append([index, height])
            
        index += 1 # out of boundary
        # if something left in stack
        while stack:
            index_pop, height_pop = stack.pop()
            if height_pop * (index - index_pop) > maxim:
                maxim = height_pop * (index - index_pop)
        return maxim