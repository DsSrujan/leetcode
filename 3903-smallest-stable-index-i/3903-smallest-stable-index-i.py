class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        p=k

        for i in range(n):
            score=(max(nums[:i+1]))-(min(nums[i:n]))
            if score<=p and score<=k:
                p=i
                return p
        return -1