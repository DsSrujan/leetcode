class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i , n in enumerate(nums):
            complement=target-n
            if complement in dic:
                return [dic[complement],i]
            else :
                dic[n]=i
        return []