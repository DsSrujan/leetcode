class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=set()
        for n in nums:
            if n in a :
                return True 
            a.add(n)
        return False