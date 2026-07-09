class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest=min(strs,key=len)
        for i in range(len(shortest)):
            for word in strs:
                if word[i]!=shortest[i]:
                    return shortest[:i]
       
        return shortest