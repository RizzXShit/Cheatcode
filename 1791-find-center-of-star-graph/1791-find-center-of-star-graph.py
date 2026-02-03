class Solution(object):
    def findCenter(self, edges):
        # n = max(max(u, v) for u, v in edges)
        # matrix = [[0] * (n + 1) for _ in range(n + 1)]
        # for u, v in edges: 
        #     matrix[u][v] = 1 
        #     matrix[v][u] = 1 
        # for i in range(1, n + 1): 
        #     if sum(matrix[i]) == n - 1: 
        #         return i

    
        n = max(max(u, v) for u, v in edges)
        graph = [[] for _ in range(n + 1)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for node in range(1, n + 1):
            if len(graph[node]) == n - 1:
                return node


