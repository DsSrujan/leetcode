class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a={}
        for num in nums:
            if num in a:
                return True 
            a[num]=a.get(num,0)+1
        return not a