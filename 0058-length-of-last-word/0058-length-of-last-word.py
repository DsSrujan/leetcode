class Solution(object):
    def lengthOfLastWord(self, s):
        i=len(s)-1
       
        count=0
        while s[i]==" ":
            i-=1
        if i ==0:
            return 1
        while s[i]!=" " and i>=0:
            count+=1
            i-=1
        return count
    
