class Solution(object):
    def getConcatenation(self, nums):
        a=[]
        for i in range(0,len(nums)):
            a.append(nums[i])
        for j in a:
            nums.append(j)
        return nums
        