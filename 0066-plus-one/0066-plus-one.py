class Solution(object):
    def plusOne(self, digits):
        i=len(digits)-1
        for i in range(i,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits 
            digits[i]=0
        return [1] + digits
            