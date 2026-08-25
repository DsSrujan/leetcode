class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        j=1
        for i in range(len(nums)+1):
            if k*j  in nums:
                j+=1
            else:
                 return k*j

        