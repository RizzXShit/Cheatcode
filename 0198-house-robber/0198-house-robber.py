class Solution(object):
    def rob(self, nums):
        c=0
        k=0
        for i in nums:
            temp=max(c+i,k)
            c=k
            k=temp
        return k


            

        