class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        m=0
        x=0
        for n in gain:
            x+=n
            m=max(m,x)
        return m