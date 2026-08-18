class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=[]
        for n in s:
            if n!="*":
                a.append(n)
            else:
                a.pop()
        return "".join(a)