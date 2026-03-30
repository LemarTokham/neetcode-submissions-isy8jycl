class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(len(self.stack)-1)

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        minNum = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < minNum:
                minNum = self.stack[i]
        return minNum
        
        
