class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        n=0
        m=0
        for i in range(len(nums)):
            if nums[i]==0:
                n+=1
            while n>k:
                if nums[l]==0:
                    n-=1
                l+=1
            m=max(m,i-l+1)
        return m
                    

                

        