class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i+1]   # sum of subarray of length 2
            if s in seen:
                return True
            seen.add(s)
        return False
