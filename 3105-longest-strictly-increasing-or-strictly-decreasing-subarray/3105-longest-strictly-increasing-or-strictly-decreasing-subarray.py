class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l=0
        m=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                m=max(m,i-l)
                l=i
        m=max(m,len(nums)-l)
        l=0
        n=0
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:
                n=max(n,i-l)
                l=i
        n=max(n,len(nums)-l)
        return max(m,n)