class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        a={}
        m=0
        for i in range(len(fruits)):
            a[fruits[i]]=a.get(fruits[i],0)+1
            while  len(a)>2:
                a[fruits[l]]-=1
                if a[fruits[l]]==0:
                    del a[fruits[l]]
                l+=1
            m=max(m,i-l+1)
        return m     

                