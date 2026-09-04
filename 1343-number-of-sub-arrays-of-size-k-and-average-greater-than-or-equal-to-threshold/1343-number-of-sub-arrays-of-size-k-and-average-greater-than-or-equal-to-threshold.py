class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        w_s = sum(arr[:k])
        count = 0
        target = threshold * k

        for i in range(k, len(arr)):
            if w_s >= target:
                count += 1

            w_s = w_s - arr[i-k] + arr[i]

        if w_s >= target:
            count += 1

        return count