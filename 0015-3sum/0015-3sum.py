class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        a=[]
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue 
            l=i+1
            r=len(nums)-1
            while l<r:
                t=nums[i]+nums[r]+nums[l]
                if t==0:
                    a.append([nums[i],nums[r],nums[l]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l< r and nums[r]==nums[r+1]:
                        r-=1
                elif t < 0:
                    l+=1
                else :
                    r-=1
        return a