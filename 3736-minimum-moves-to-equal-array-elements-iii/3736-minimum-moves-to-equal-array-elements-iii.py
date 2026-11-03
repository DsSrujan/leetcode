class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        return max(nums)*len(nums)-sum(nums)
