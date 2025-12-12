class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        minX, maxX, minY, maxY = {}, {}, {}, {}

        # Precompute row and column extremes
        for x, y in buildings:
            minX[y] = x if y not in minX else min(minX[y], x)
            maxX[y] = x if y not in maxX else max(maxX[y], x)
            minY[x] = y if x not in minY else min(minY[x], y)
            maxY[x] = y if x not in maxY else max(maxY[x], y)

        cnt = 0
        for x, y in buildings:
            if minX[y] < x < maxX[y] and minY[x] < y < maxY[x]:
                cnt += 1
        return cnt
