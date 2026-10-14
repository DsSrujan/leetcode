class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Step 1: Feasibility Check
        # The largest digit we can use is 9. 
        # If the requested sum is larger than num * 9, it's impossible to form the number.
        if sum > num * 9:
            return ""
            
        # Step 2: Greedy Allocation
        # To maximize the sum of squares, we need to concentrate values into '9's.
        # To maximize the numeric value, these '9's must go as far left as possible.
        nines = sum // 9
        remainder = sum % 9
        
        # Step 3: String Construction
        result = []
        result.append("9" * nines)
        
        # If there is a leftover remainder digit, place it right after the 9s
        if remainder > 0:
            result.append(str(remainder))
            
        # Pad the rest of the positions with zeros to reach the required 'num' length
        zeros_needed = num - len(result[0]) - (1 if remainder > 0 else 0)
        result.append("0" * zeros_needed)
        
        return "".join(result)
