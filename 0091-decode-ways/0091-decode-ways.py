class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [-1] * (n+1)
        def decode(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if dp[i] != -1:
                return dp[i]
            ways = decode(i+1)
            if i+1 < n and int(s[i:i+2]) <= 26:
                ways += decode(i+2)
            dp[i] = ways
            return dp[i]
        return decode(0)
