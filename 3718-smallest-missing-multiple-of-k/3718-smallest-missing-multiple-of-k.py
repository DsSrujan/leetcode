class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        j=1
        for i in range(len(nums)+1):
            if k*j not in nums:
                return k*j
            j+=1

        