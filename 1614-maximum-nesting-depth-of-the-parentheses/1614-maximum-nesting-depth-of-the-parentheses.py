class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        m=0
        for n in s:
            if n =="(":
                c+=1
                m=max(c,m)
            elif n==")":
                c-=1
        return m
                
        