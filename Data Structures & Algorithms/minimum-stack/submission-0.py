class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        val = min(value,self.minstack[-1] if self.minstack else value)
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
