class MinStack(object):

    def __init__(self):
        self.stack = []
        self.Minstack = []

    def push(self, value):
        self.stack.append(value)

        b = len(self.Minstack)

        while b and value > self.Minstack[b - 1]:
            b -= 1

        self.Minstack.insert(b, value)

    def pop(self):
        value = self.stack.pop()

        for i in range(len(self.Minstack)):
            if self.Minstack[i] == value:
                self.Minstack.pop(i)
                break

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.Minstack[-1]