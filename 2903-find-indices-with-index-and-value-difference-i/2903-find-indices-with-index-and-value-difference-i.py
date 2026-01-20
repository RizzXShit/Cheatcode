class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        
        cnt=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(j-i)>=indexDifference and abs(nums[j]-nums[i])>=valueDifference:
                    return [i,j]
        return [-1,-1]
        