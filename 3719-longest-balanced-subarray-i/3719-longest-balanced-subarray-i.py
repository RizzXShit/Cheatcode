class Solution(object):
    def longestBalanced(self, nums):
        res=0;
        for i in range(len(nums)):
            e=set();
            o=set();
            for j in range(i,len(nums)):
                if(nums[j]%2==0):
                    e.add(nums[j])
                else:
                    o.add(nums[j]);
                if(len(e)==len(o)):
                    res=max(res,j-i+1)
        return res