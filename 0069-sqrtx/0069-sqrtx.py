class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        g = x
        
        while g * g > x:
            g = (g + x // g) // 2
        
        return g