class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        w_a=sum(nums[:k])
        m=w_a
        for i in range(k,len(nums)):
            w_a+=nums[i]-nums[i-k]
            if w_a>m:
                m=w_a
        return m/k
