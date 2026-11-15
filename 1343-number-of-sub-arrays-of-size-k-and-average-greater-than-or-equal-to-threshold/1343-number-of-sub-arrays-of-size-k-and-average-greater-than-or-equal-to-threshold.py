class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        s=sum(arr[:k])
        c= 1 if s >= threshold * k else 0
        w_s=s
        for i in range(k,len(arr)):
            w_s+=arr[i]-arr[i-k]
            if w_s >= threshold * k:
                c+=1
        return c

        