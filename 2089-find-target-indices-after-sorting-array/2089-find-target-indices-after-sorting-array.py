class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        a=[]
        for i , n in enumerate(nums):
            if n==target:
                a.append(i)
        return a