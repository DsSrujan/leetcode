class Solution:
    def countElements(self, nums: list[int]) -> int:
        c=0
        m=max(nums)
        n=min(nums)
        for i in range(len(nums)):
            if n<nums[i]<m:
                c+=1
        return c