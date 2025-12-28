class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(grid)-1, -1, -1):          
            for j in range(len(grid[i])-1, -1, -1):   
                if grid[i][j] < 0:
                    cnt += 1
                else:
                    break   
        return cnt
