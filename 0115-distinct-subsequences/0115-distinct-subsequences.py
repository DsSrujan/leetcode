class Solution(object):
    def numDistinct(self, s, t):

        memo = {}

        def solve(i, j):

            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                take = solve(i + 1, j + 1)
                skip = solve(i + 1, j)

                memo[(i, j)] = take + skip

            else:
                memo[(i, j)] = solve(i + 1, j)

            return memo[(i, j)]

        return solve(0, 0)