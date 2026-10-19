class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        answer =[1]*n
        r=1
        for i in range(n):
            answer[i]=r
            r*=nums[i]
        l=1
        for i in range(n-1,-1,-1):
            answer[i]*=l
            l*=nums[i]
        return answer
        