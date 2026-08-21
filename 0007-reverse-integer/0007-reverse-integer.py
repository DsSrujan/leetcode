class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        re=0
        a=x*-1 if x<0 else x
        for i in range(len(str(a))):
            re=re*10+a%10
            a//=10
        y = re*-1 if x<0 else re
        if y > 2147483647 or y < -2147483648:
            return 0
        return y
    

        