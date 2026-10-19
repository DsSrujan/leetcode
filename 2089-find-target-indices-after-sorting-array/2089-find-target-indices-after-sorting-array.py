class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                a.append(i)
        return a

        