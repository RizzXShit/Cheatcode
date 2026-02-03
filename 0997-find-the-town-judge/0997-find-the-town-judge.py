class Solution(object):
    def findJudge(self, n, trust):
        # """
        # :type n: int
        # :type trust: List[List[int]]
        # :rtype: int
        # """
        # if all(trust[i][1]==n for i in range(len(trust))):
        #     return n
        # else:
        #     return -1
        matrix = [[0] * (n + 1) for _ in range(n + 1)] 
        for u, v in trust: 
            matrix[u][v] = 1 
            
        for person in range(1, n + 1): 
            if sum(matrix[person]) == 0:
                trusted_count = sum(matrix[i][person] for i in range(1,n+1))
                if trusted_count==(n-1):
                    return person 
        return -1

        
        