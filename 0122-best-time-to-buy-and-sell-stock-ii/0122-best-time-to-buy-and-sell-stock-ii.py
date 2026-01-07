class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        memo={}
        def dfs(i, holding):
            
            if i == n:
                return 0
            if (i,holding) in memo:
                return memo[(i,holding)]
            res = dfs(i+1, holding)
            if holding:
                res = max(res, prices[i] + dfs(i+1, 0))
            else:
                res = max(res, -prices[i] + dfs(i+1, 1))
            
            memo[(i,holding)]=res
            return res
        
        return dfs(0, 0)
