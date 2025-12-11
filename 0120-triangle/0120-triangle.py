class Solution(object):
    def minimumTotal(self, triangle):
        m=len(triangle)
        def lol(i,j):
            if i == 0 and j == 0:
                return triangle[0][0]
            if j < 0 or j > i:
                return float('inf') 
            return triangle[i][j] + min(lol(i-1, j-1), lol(i-1, j))
        last = m - 1
        return min(lol(last, j) for j in range(last+1))

        