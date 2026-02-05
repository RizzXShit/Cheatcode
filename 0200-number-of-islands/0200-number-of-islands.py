class Solution(object):
    def numIslands(self, grid):
        m=len(grid)
        n=len(grid[0])
        cnt=0
        visit=set()
        def dfs(m,n):
            if m<0 or n<0 or m>=len(grid) or n>=len(grid[0]) or grid[m][n]=='0' or (m,n) in visit:
                return
            visit.add((m,n))
            
            dfs(m-1,n)
            dfs(m,n-1)
            dfs(m+1,n)
            dfs(m,n+1)

        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visit :
                    dfs(i,j)
                    cnt+=1
        return cnt

        
        