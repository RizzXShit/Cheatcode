class Solution(object):
    def canPartition(self, arr):
        total = sum(arr)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(arr)

        dp = [[None] * (target + 1) for _ in range(n)]

        def solve(idx, t):
            if t == 0:
                return True
            if idx < 0:
                return False
            if dp[idx][t] is not None:
                return dp[idx][t]

            exc = solve(idx - 1, t)

            inc = False
            if arr[idx] <= t:
                inc = solve(idx - 1, t - arr[idx])

            dp[idx][t] = exc or inc
            return dp[idx][t]

        return solve(n - 1, target)
