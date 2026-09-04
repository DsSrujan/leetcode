class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        w_s=sum(nums[:k])
        maxi=w_s
        for i in range(k,len(nums)):
            w_s = w_s-nums[i-k]+nums[i]
            maxi=max(w_s, maxi)
        return maxi/float(k)
        