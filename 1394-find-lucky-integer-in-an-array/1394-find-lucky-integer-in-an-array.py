class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m=0
        a={}
        for i in arr:
            a[i]=a.get(i,0)+1
        print(a)
        for  k in a.keys():
            if k==a[k]:
                m=max(m,k)
        return m if m else -1

