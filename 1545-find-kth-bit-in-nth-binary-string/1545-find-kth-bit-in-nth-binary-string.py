class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def invert(s):
            return ''.join('1' if ch=='0' else '0' for ch in s)
        def cntsn(n):
            if n==1:
                return "0"
            prev=cntsn(n-1)
            return prev+"1"+invert(prev[::-1])
        a=cntsn(n)
        return a[k-1]
        