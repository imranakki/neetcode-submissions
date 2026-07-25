class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        L = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:

                num1 = L[-1]
                L.pop()
                num2 = L[-1]
                L.pop()

                L.append(str(int(eval(num2 + i + num1))))
            else:
                L.append(i)
        return int(L[0])
