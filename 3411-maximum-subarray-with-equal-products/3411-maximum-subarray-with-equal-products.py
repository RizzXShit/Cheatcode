class Solution:
    def maxLength(self, nums: List[int]) -> int:

        n, ans = len(nums), 2

        for i in range(n - 1):
            gcd_ = lcm_ = nums[i]
          
            for j in range(i + 1, n):
                gcd_ = gcd(gcd_, nums[j])

                if gcd_ != 1 or gcd(lcm_, nums[j]) != 1:
                    ans = max(ans, j - i)
                    break

                lcm_*= nums[j]

            else: ans = max(ans, j - i + 1)

        return ans