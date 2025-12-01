class Solution(object):
    def minOperations(self, nums, k):
        cnt=0
        for i in nums:
            cnt+=i
        return cnt%k
        