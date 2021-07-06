class Solution:
    def isValid(self, s: str) -> bool:
        
        queue = deque()
        
        for val in s:
            if val == '(' or val == '[' or val == '{':
                queue.append(val)
            elif val == ')':
                if not queue or queue.pop() !='(':
                    return(False)
            elif val == '}':
                if not queue or queue.pop() !='{':
                    return(False)
            elif val == ']':
                if not queue or queue.pop() !='[':
                    return(False)
        if queue:
            return(False)
        return(True)