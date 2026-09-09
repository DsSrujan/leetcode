class Solution(object):
    def subarraySum(self, nums, k):
        c = 0
        prefix = 0
        freq = {0: 1}

        for n in nums:
            prefix += n

            needed = prefix - k

            if needed in freq:
                c += freq[needed]

            freq[prefix] = freq.get(prefix, 0) + 1

        return c