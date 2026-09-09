class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={}
        for num in s:
            a[num]=a.get(num,0)+1
        for num, i in enumerate(s):
            if a[i]==1:
                return num
        return -1