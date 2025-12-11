class Solution(object):
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        def minval(i,j):
            if i<0 or j<0:
                return float('inf')
            if i==0 and j==0:
                return grid[0][0]
            if dp[i][j]!=-1:
                return dp[i][j]

            a= grid[i][j]+min(minval(i-1,j),minval(i,j-1))
            dp[i][j]=a
            return a
        return minval(m-1,n-1)

            

        