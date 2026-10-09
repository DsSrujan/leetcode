class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n=len(nums)
        a=[0]*n
        for i in  range(n):
            a[nums[i]-1]+=1
        for i in range(n):
            if a[i]==0:
                b=i+1
            if a[i]==2:
                c=i+1
        return [c,b]
            

        