class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                queue = [i]
                visited[i] = True
                while queue:
                    city = queue.pop(0)  
                    for j in range(n):
                        if isConnected[city][j] == 1 and not visited[j]:
                            visited[j] = True
                            queue.append(j)
                provinces += 1
        return provinces
