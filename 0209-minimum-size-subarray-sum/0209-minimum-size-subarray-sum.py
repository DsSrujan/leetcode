class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        w_s=0
        m=float('inf')
        l=0
        for i in range(len(nums)):
            w_s+=nums[i]
            while w_s>=target :
                m=min(m,i-l+1)
                w_s-=nums[l]
                l+=1
        return 0 if m==float('inf') else m


        