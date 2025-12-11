class Solution(object):
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for _ in range(m)]
        '''def minval(i,j):
            if i<0 or j<0:
                return float('inf')
            if i==0 and j==0:
                return grid[0][0]
            if dp[i][j]!=-1:
                return dp[i][j]

            a= grid[i][j]+min(minval(i-1,j),minval(i,j-1))
            dp[i][j]=a
            return a
        return minval(m-1,n-1)'''
        dp[0][0]=grid[0][0]
        for i in range(1,n):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        for j in range(1,m):
            dp[j][0]=dp[j-1][0]+grid[j][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]


            

        