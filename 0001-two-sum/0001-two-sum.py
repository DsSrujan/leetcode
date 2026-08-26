class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i,n in enumerate(nums):
            compliment=target-n
            if compliment in dic:
                return [dic[compliment],i]
            dic[n]=i