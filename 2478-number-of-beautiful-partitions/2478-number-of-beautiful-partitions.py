class Solution:
    def beautifulPartitions(self, s: str, k: int, mn: int) -> int:
        n = len(s)
        mn = max(mn, 2)
        mod = 10 ** 9 + 7
        
        def isPrime(x) -> bool:
            return x == '2' or x == '3' or x == '5' or x == '7'
        
        @lru_cache(maxsize=None)
        def dp(i, rem, isActive) -> int:
            if rem < 0: return 0
            if i >= n:
                return rem == 0 and isActive == 0
            res = 0
            if not isActive:
                if not isPrime(s[i]): return 0
                res = (res + dp(i + mn - 1, rem - 1, 1)) % mod
            else:
                res = (res + dp(i + 1, rem, 1)) % mod
                if not isPrime(s[i]):
                    res = (res + dp(i + 1, rem, 0)) % mod
            return res
        
        return dp(0, k, 0)