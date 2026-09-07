class Solution(object):
    def lengthOfLongestSubstring(self, s):
        c=set()
        l=0
        maxi=0
        for i in range(len(s)):
            while s[i] in c:
                c.remove(s[l])
                l+=1
                
            c.add(s[i])
            maxi=max(maxi,i-l+1)
        return maxi
        
        