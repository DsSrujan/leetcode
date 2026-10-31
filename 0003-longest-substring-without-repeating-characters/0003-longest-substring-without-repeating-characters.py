class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        maxi=0
        l=0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[l])
                l+=1
            a.add(s[i])
            maxi=max(maxi, i-l+1)
        return maxi
        
        
        