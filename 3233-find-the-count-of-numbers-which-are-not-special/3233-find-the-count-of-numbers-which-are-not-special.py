class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        mn, mx = ceil(sqrt(l)), isqrt(r) 

        sieve = [False, False, True]
        sieve.extend([True, False] * (mx//2))

        for p in range(3, mx+1, 2):
            if not sieve[p]: continue
            for i in range(p * p, mx+1, p+p): sieve[i] = False
   
        return r - l + 1 - sum(sieve[mn:mx+1])