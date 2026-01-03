class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left = 0
        su = 0
        minn = float('inf')

        for right in range(n):
            su += nums[right]
            while su >= target:
                minn = min(minn, right - left + 1)
                su -= nums[left]
                left += 1

        return 0 if minn == float('inf') else minn
