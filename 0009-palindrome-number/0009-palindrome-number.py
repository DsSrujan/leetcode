class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        n=x
        while n > 0:
            d=n%10
            r=r*10+d
            n//=10
        return r==x