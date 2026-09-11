
class Solution(object):
    def totalNumbers(self, digits):
        count = 0

        for a in range(1, 10):       # hundreds: cannot be 0
            for b in range(10):      # tens
                for c in range(0, 10, 2):  # ones: must be even

                    num = [a, b, c]

                    # check if these digits can be formed
                    temp = digits[:]
                    possible = True

                    for x in num:
                        if x in temp:
                            temp.remove(x)
                        else:
                            possible = False
                            break

                    if possible:
                        count += 1

        return count
