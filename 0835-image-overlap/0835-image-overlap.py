class Solution(object):
    def largestOverlap(self, img1, img2):
        shifts = {}

        for r1 in range(len(img1)):
            for c1 in range(len(img1)):
                if img1[r1][c1] == 1:

                    for r2 in range(len(img2)):
                        for c2 in range(len(img2)):
                            if img2[r2][c2] == 1:

                                dr = r2 - r1
                                dc = c2 - c1

                                shifts[(dr, dc)] = shifts.get((dr, dc), 0) + 1

        if shifts:
            return max(shifts.values())
        return 0