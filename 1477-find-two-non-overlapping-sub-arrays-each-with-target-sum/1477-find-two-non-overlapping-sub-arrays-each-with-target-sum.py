class Solution(object):
    def minSumOfLengths(self,arr, target):
        n = len(arr)
        prefix = [float('inf')] * n
        res = float('inf')
        s = left = 0
        best = float('inf')

        for right in range(n):
            s += arr[right]
            while s > target:
                s -= arr[left]
                left += 1
            if s == target:
                length = right - left + 1
                if left > 0:
                    res = min(res, length + prefix[left - 1])
                best = min(best, length)
            prefix[right] = best
        return res if res != float('inf') else -1
