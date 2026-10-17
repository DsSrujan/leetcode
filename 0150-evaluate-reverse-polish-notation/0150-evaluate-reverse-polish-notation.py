class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        a=[]
        for  n in tokens:
            if n == "+":
                a.append(a.pop()+a.pop())
            elif n=="*":
                a.append(a.pop()*a.pop())
            elif n=="-":
                a.append((a.pop()-a.pop())*-1)
            elif n=="/":
                x=a.pop()
                y=a.pop()
                a.append(int(y/x))
            else:
                a.append(int(n))
        return a[-1]

        