class Solution(object):
    def targetIndices(self, nums, target):
        a=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                a.append(i)
        return a

        