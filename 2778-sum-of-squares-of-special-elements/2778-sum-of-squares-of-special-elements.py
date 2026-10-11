class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s=0
        j=2
        for i in range(1,len(nums)):
            if len(nums)%j==0:
                s+=nums[i]**2
            j+=1
        return nums[0]**2+s
        