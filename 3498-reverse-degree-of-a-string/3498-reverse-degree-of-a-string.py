class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        for i , a in enumerate(s,start=1):
            r+=((91-ord(a.upper()))*i)
        return r
            
        