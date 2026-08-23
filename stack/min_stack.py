class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.minVal = val
            self.stack.append(val - self.minVal)
        elif val < self.minVal:
            self.stack.append(val - self.minVal)
            self.minVal = val
        else:
            self.stack.append(val - self.minVal)

    def pop(self) -> None:
        top = self.stack.pop()
        if top < 0:
            self.minVal -= top

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.minVal
        return self.stack[-1] + self.minVal

    def getMin(self) -> int:
        return self.minVal


class MinStackTwo:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
