class Solution:
    def twoSum(self, nums, target):
        d={}
        for i ,n in enumerate(nums):
            compliment=target-n
            if compliment in d:
                return [d[compliment],i]
            d[n]=i