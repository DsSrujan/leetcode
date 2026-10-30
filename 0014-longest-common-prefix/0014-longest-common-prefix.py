class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        m=min(strs,key =len)
        for i in range(len(m)):
            for s in strs:
                if s[i]!=m[i]:
                    return m[:i]
        return m        