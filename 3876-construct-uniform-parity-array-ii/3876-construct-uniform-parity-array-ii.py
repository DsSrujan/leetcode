class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        smallest = min(nums1)

        for n in nums1:
            if n % 2 != smallest % 2:
                if smallest % 2 == 0:
                    return False

        return True