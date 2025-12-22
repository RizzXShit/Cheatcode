class Solution(object):
    def coinChange(self, coins, amount):
        # memo = {}
        
        # def dp(x):
        #     if x == 0:
        #         return 0
        #     if x < 0:
        #         return float('inf')
        #     if x in memo:
        #         return memo[x]
            
        #     ans = float('inf')
        #     for coin in coins:
        #         ans = min(ans, 1 + dp(x - coin))
            
        #     memo[x] = ans
        #     return ans
        
        # res = dp(amount)
        # return res if res != float('inf') else -1


        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],dp[i-j]+1)

        return dp[amount] if dp[amount]!=amount+1 else -1
