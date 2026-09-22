class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If there's only 1 row or the string is shorter than rows,
        # the zigzag pattern matches the original string.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an empty string array for each row
        rows = [""] * numRows
        current_row = 0
        direction = -1  # Controls moving down (1) or up (-1)
        
        for char in s:
            rows[current_row] += char
            
            # Reverse direction when hitting the top (0) or bottom (numRows - 1) row
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
                
            current_row += direction
            
        # Combine all rows to form the final string
        return "".join(rows)
