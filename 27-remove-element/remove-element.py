class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # Pointer for the next position of a valid element
        
        for i in range(len(nums)):
            # If the current element is not the one we want to remove
            if nums[i] != val:
                nums[k] = nums[i]  # Move it to the front
                k += 1             # Increment the count of valid elements
                
        return k