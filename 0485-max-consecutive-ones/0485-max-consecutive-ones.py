class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                c=0
            m=max(m,c)
        return m
        