class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        a=[]
        for i in range(len(nums)-2):
            r=i+1
            l=len(nums)-1
            if i > 0 and nums[i]==nums[i-1]:
                continue 
            while r<l:
                t=nums[i]+nums[r]+nums[l]
                if t==0:
                    a.append([nums[i],nums[r],nums[l]])
                    r+=1
                    l-=1
                    while r<l and nums[r]==nums[r-1]:
                        r+=1
                    while r<l and nums[l]==nums[l+1]:
                        l-=1
                elif t < 0:
                    r+=1
                else :
                    l-=1
        return a 
                