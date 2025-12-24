class Solution(object):
    def minInsertions(self, s):
        i=0
        j=len(s)-1
        memo={}
        def solve(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i>=j:
                return 0
            if s[i]==s[j]:
                return solve(i+1,j-1)
            
            else:
                a= min(1+solve(i+1,j),1+solve(i,j-1))
                memo[(i,j)]=a
                return a
        return solve(i,j)