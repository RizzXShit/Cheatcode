class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[(i + v) % len(nums)] for i, v in enumerate(nums)]