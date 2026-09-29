class Solution(object):
    def findLucky(self, arr):
        
        m=-1
        a={}
        for i in arr:
            a[i]=a.get(i,0)+1
        print(a)
        for  k in a.keys():
            if k==a[k]:
                m=max(m,k)
        return m 

