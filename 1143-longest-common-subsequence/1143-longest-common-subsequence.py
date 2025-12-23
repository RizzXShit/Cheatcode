

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        m, n = len(text1), len(text2)
        memo={}
        def dfs(i, j):
            if i == m or j == n:
                return 0

            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            
            if (i,j) in memo:
                return memo[(i,j)]

            me=max(dfs(i + 1, j), dfs(i, j + 1))
            memo[(i,j)]=me
            return me

        return dfs(0, 0)
