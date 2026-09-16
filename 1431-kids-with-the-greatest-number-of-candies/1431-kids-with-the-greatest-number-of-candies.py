class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]

        """
        m=max(candies)
        a=[]
        for  n in candies:
            if n+extraCandies>=m:
                a.append(True)
            else :
                a.append(False)
        return a
