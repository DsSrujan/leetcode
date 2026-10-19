class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        w_s=sum(nums[:k])
        maxi=w_s
        for i in range(k, len(nums)):
            w_s=w_s-nums[i-k]+nums[i]
            if w_s>maxi:
                maxi=w_s
        return maxi/k
        
        