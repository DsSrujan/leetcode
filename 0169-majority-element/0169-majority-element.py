class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        n=len(nums)
        for i in nums:
            a[i]=a.get(i,0)+1
        for j in nums:
            if a[j]>n/2:
                return j
