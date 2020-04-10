class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = None
        self.min = None

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.insert(0,x)
            self.min.insert(0,min(x,self.min[0] if self.min else x))
        else:
            self.stack = [x]
            self.min = [x]

    def pop(self) -> None:
        if self.stack:
            del self.stack[0]
            del self.min[0] 
        

    def top(self) -> int:
        return self.stack[0] if self.min else None
        

    def getMin(self) -> int:
        return self.min[0] if self.min else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
