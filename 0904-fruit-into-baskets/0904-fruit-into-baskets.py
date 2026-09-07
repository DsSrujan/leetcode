class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        maxi=0
        s={}
        for i in range(len(fruits)):
            s[fruits[i]]=s.get(fruits[i],0)+1

            while len(s)>2:
                s[fruits[l]]-=1
                if s[fruits[l]]==0:
                    del s[fruits[l]]
                l+=1
            maxi=max(maxi,i-l+1)
        return maxi


                    