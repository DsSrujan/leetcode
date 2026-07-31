class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        # Store left products
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # Multiply with right products
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer