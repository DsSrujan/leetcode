class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars=set()
        l=0
        for ch in s :
            if ch in chars:
                chars.remove(ch)
                l+=2
            else:
                chars.add(ch)
        if chars:
            l+=1
        return l
