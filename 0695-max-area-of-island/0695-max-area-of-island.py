class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        ma=0
        visit=set()
        def dfs(m,n):
            
            if m<0 or n<0 or m>=len(grid) or n>=len(grid[0]) or grid[m][n]==0 or (m,n) in visit:
                return 0
            visit.add((m,n))
            
            return (1+dfs(m-1,n)+dfs(m,n-1)+dfs(m+1,n)+dfs(m,n+1))
            

        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visit :
                    a=dfs(i,j)
                    if a>ma:
                        ma=a
                    
        return ma
