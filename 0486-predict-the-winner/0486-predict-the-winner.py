class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def scoreDiff(l, r):
            if l == r:
                return nums[l]
            pickLeft = nums[l] - scoreDiff(l+1, r)
            pickRight = nums[r] - scoreDiff(l, r-1)
            return max(pickLeft, pickRight)

        return scoreDiff(0, len(nums)-1) >= 0




        