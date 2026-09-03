class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2=[]
        for n in nums:
            if n%2==0:
                nums2.insert(0,n)
            else:
                nums2.append(n)
        return nums2