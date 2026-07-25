class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []    
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        mn = val
        if(self.minStack and self.minStack[-1] < mn) :
            mn = self.minStack[-1]
        self.minStack.append(mn)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
