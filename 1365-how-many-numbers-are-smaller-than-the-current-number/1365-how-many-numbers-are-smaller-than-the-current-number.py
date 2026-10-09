class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        f={}
        for i, n in enumerate(sorted(nums)):
            if n not in f:
                f[n]=i
        for i,  n in enumerate(nums):
            nums[i]=f[n]
        return nums



        
        