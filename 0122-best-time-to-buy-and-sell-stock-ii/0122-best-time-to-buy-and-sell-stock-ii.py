class Solution:
    def maxProfit(self, prices):
        # n = len(prices)
        # memo={}
        # def dfs(i, holding):
            
        #     if i == n:
        #         return 0
        #     if (i,holding) in memo:
        #         return memo[(i,holding)]
        #     res = dfs(i+1, holding)
        #     if holding:
        #         res = max(res, prices[i] + dfs(i+1, 0))
        #     else:
        #         res = max(res, -prices[i] + dfs(i+1, 1))
            
        #     memo[(i,holding)]=res
        #     return res
        
        # return dfs(0, 0)
        n = len(prices) 
        dp = [[0, 0] for _ in range(n+1)] 
        for i in range(n-1, -1, -1): 
            dp[i][0] = max(dp[i+1][0], -prices[i] + dp[i+1][1]) 
            dp[i][1] = max(dp[i+1][1], prices[i] + dp[i+1][0]) 
        return dp[0][0]

#__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))


