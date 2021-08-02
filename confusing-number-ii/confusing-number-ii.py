class Solution:
    def confusingNumberII(self, n: int) -> int:
        # Backtracking O(logn)
        possible_confuse = ["0", "1", "6", "8", "9"]
        
        hashMap = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6"
        }
        
        def dfs(node):
            count_result = 0
            if int(node) > n:
                return count_result

            rotated_num = ''
            for i in reversed(node):
                rotated_num = rotated_num + hashMap[i]

            if int(node) <= n and rotated_num != node:
                count_result += 1

            for val in possible_confuse:
                count_result += dfs(node + val)

            return count_result

        result = 0
        for node in possible_confuse[1:]:
            result += dfs(node)

        return result