import heapq

class Solution(object):
    def networkDelayTime(self,times, n, k):
        g = [[] for _ in range(n+1)]
        for u,v,w in times:
            g[u].append((v,w))
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        h = [(0,k)]
        while h:
            d,u = heapq.heappop(h)
            if d > dist[u]:
                continue
            for v,w in g[u]:
                if dist[v] > d+w:
                    dist[v] = d+w
                    heapq.heappush(h,(dist[v],v))
        ans = max(dist[1:])
        if ans==float('inf'):
            return -1
        else:
            return ans
