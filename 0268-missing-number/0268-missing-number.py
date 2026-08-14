class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Old python compatible integer division formula
        expected_sum = (n * (n + 1)) / 2
        
        # Calculate sum of elements present
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum
