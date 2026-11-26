class Solution:
    def canAliceWin(self, n: int) -> bool:
        i=0
        if n < 10:
            return False 
        
        while n>=0:
            n-=(10-i)
            i+=1
        return i%2==0 
        