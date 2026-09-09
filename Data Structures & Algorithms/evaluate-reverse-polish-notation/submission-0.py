import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        N=len(tokens)
        for i in range(N):
            if tokens[i].lstrip("-").isnumeric():
                stack.append(int(tokens[i]))
            else:
                a=stack.pop()
                b=stack.pop()
                if tokens[i] == "+":
                    stack.append(b+a)
                elif tokens[i] == "-":
                    stack.append(b-a)
                elif tokens[i] == "*":
                    stack.append(b*a)
                elif tokens[i] == "/":
                    stack.append(int(b/a))
                else:return 0
        return stack.pop()
                