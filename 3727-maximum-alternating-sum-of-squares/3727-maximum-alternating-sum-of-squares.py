class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i ,n in enumerate(nums):
            nums[i]=n**2
        nums.sort()
        n=len(nums)
        m=n//2
        return sum(nums[m:n])-sum(nums[:m])
        