class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i, n in enumerate(nums):
            c=target-n
            if c in dic:
                return [dic[c],i]
            dic[n]=i