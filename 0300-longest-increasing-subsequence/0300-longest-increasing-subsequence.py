class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        dp = [1] * n 
        ma = 0 
        for i in range(n): 
            for j in range(i): 
                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i], dp[j] + 1) 
            ma = max(ma, dp[i]) 
        return ma