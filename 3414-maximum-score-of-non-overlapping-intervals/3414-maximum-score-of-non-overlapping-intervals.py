from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):

        n = len(intervals)

        # Store original index
        intervals = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        starts = [x[0] for x in intervals]

        # dp[i][k] = best answer from i onwards
        # when we can still choose k intervals
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            l, r, w, index = intervals[i]

            # First interval with start > r
            j = bisect_right(starts, r)

            for k in range(1, 5):

                # Skip current interval
                skip = dp[i + 1][k]

                # Take current interval
                next_score, next_indices = dp[j][k - 1]

                take = (
                    w + next_score,
                    tuple(sorted((index,) + next_indices))
                )

                if take[0] > skip[0]:
                    dp[i][k] = take
                elif take[0] < skip[0]:
                    dp[i][k] = skip
                else:
                    dp[i][k] = min(take, skip)

        return list(dp[0][4][1])