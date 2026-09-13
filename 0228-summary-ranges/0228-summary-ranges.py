
class Solution(object):
    def summaryRanges(self, nums):
        i = 0
        j = 1
        b = []
        if not nums:
            return []

        while j < len(nums):
            if nums[j] - nums[j - 1] == 1:
                j += 1
            else:
                if i == j - 1:
                    b.append(str(nums[i]))
                else:
                    b.append(str(nums[i]) + "->" + str(nums[j - 1]))

                i = j
                j += 1

        # process the last range
        if i == len(nums) - 1:
            b.append(str(nums[i]))
        else:
            b.append(str(nums[i]) + "->" + str(nums[-1]))

        return b

