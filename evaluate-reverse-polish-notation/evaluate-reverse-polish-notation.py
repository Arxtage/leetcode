class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(N)
        # use stack
        
        stack = []
        
        operators = set(["+","-", "*", "/"])
        
        for val in tokens:
            if val in operators:
                b = stack.pop()
                a = stack.pop()
                if val == '+':
                    stack.append(a+b)
                elif val == '-':
                    stack.append(a-b)
                elif val == '*':   
                    stack.append(a*b)
                else:
                    if a//b < 0:
                        stack.append(- (abs(a)//abs(b)) )
                    else:
                        stack.append(a//b)

            else:
                stack.append(int(val))
        return stack[0]
                    