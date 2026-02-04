class Solution(object):
    def validPath(self, n, edges, source, destination):
        gr=[[] for _ in range(n)]
        for u, v in edges:
            gr[u].append(v)
            gr[v].append(u)

        vi= [False] * n
        q = [source]
        vi[source] = True

        while q:
            node = q.pop(0)
            if node == destination:
                return True
            for i in gr[node]:
                if not vi[i]:
                    vi[i] = True
                    q.append(i)
        return False
