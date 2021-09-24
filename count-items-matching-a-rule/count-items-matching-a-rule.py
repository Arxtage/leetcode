class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # O(n)
        res = 0
        
        if ruleKey == 'type':
            index = 0
        if ruleKey == 'color':
            index = 1
        if ruleKey == 'name':
            index = 2
            
        for item in items:
            if item[index] == ruleValue:
                res += 1
                
        return res
            