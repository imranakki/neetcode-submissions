class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if(not stack):
                stack.append(tokens[i])
            else:
                if(tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/'):
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(str(int(eval(b+tokens[i]+a))))
                else:
                    stack.append(tokens[i])
        return int(stack[-1])
                