class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a =set()
        l=0
        m=0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[l])
                l+=1
            a.add(s[i])
            b=i-l+1
            if b> m:
                m=b
        return m

        