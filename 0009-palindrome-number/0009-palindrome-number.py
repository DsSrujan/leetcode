class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        if x<0 or (x%10==0 and x!=0):
            return False 
        while x > r:
            r=r*10+x%10
            x//=10
        return x ==r or x==r//10
