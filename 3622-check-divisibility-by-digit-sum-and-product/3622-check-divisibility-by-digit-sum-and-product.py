class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        su=0
        prod=1
        a=[]
        b=n
        while b:
            a.append(b%10)
            b//=10
        for x in a:
            su+=x
            prod*=x
        return n%(su+prod)==0
        