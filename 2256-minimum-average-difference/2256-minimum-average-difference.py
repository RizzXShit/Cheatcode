class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        minn = float('inf')
        ri = 0

        for i in range(n):
            prefix_sum += nums[i]
            leftav = prefix_sum // (i + 1)

            if i == n - 1:
                riav = 0   
            else:
                riav = (total_sum - prefix_sum) // (n - i - 1)

            av = abs(leftav - riav)
            if av < minn:
                minn = av
                ri = i

        return ri
