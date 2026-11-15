class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        w_a=sum(nums[:k])
        m=w_a
        for i in range(k,len(nums)):
            w_a+=nums[i]-nums[i-k]
            m=max(w_a,m)
        return m/k
