class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sr=set("aeiouAEIOU")
        c=0
        m=0
        for i in range(len(s)):
            if s[i] in sr:
                c+=1
            if i>=k:
                c=c-1 if s[i-k] in sr else c
            if c>m:
                m=c
        return m

        