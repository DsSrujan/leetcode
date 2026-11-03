class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        t=0
        for i in range(len(nums)):
            t+=m-nums[i]
        return t
