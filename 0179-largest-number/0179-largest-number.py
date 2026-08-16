from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        # Convert integers to strings
        num_strs = [str(num) for num in nums]
        
        # Custom comparison function
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using the key wrapper
        num_strs.sort(key=cmp_to_key(compare))
        
        # Join strings
        largest_num = "".join(num_strs)
        
        # Handle trailing/leading zeros edge case
        return "0" if largest_num[0] == "0" else largest_num
