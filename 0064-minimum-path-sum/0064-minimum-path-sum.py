class Solution(object):
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        memo={}
        def minval(grid,i,j):
            minn=0
            if i<0 or j<0:
                return float('inf')
            if i==0 and j==0:
                return grid[0][0]
            if (i,j) in memo:
                return memo[(i,j)]

            a= grid[i][j]+min(minval(grid,i-1,j),minval(grid,i,j-1))
            memo[(i,j)]=a
            return a
        return minval(grid,m-1,n-1)

            

        