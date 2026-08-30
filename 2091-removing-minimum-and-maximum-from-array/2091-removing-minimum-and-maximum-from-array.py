class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=0
        maxi=0
        for  i,n in enumerate(nums):
            mini=i if n<nums[mini] else mini
            maxi=i if n>nums[maxi] else maxi
        n=len(nums)
        a = max(mini, maxi) + 1
        b = n - min(mini, maxi)
        c = min(mini, maxi) + 1 + n - max(mini, maxi)
        return min(a,b,c)
        