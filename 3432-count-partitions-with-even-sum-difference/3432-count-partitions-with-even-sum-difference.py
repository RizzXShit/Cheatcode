class Solution(object):
    def countPartitions(self, nums):
        a=[]
        cnt=0
        for i in range(len(nums)-1):
            a.append(sum(nums[0:i+1])-sum(nums[i+1:]))
        for j in a:
            if j%2==0:
                cnt+=1
        return cnt
