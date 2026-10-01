class Solution(object):
    def isValid(self, s):
        d={")":"(","}":"{","]":"["}
        a=[]
        for n in s:
            
            if n in "({[":
                a.append(n)
            else:
                if  not a :
                    return False
                if a[-1]!=d[n]:
                    return False
                a.pop() 
                
        return len(a)==0