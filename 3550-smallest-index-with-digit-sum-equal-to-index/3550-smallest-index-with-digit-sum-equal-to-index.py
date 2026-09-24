class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for  i , n in enumerate(nums):
            s=0
            if n<10  and n==i:
                return i
            
            while n>0:
                s+=n%10
                n//=10
            if s==i:
                return i
        return -1
                
                

        