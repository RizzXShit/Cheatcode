class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ma=0
        for i in range(2,len(nums)):
            a=nums[i-2]
            b=nums[i-1]
            c=nums[i]
            if a+b>c and b+c>a and a+c>b:
                if a+b+c>ma:
                    ma=a+b+c
        return ma