class Solution(object):
    def removeOuterParentheses(self, s):
        
        a=-1
        b=[]
        for n in s:
            if n=="(":
                a+=1
            if a>0:
                b.append(n)
            if n==")":
                a-=1
        return "".join(b)

        