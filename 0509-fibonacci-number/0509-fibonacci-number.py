class Solution(object):
    '''def fib(self, n):
        dp=[-1]*(n+1)
        return self.solve(n,dp)
        
              
        
    def solve(self,n,dp):
        if n==0 or n==1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.solve(n-1,dp)+self.solve(n-2,dp)
        return dp[n]'''
    def fib(self,n):
        dp=[-1]*(n+1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.solve(n,dp)
        
              
        
    def solve(self,n,dp):
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    
    
        