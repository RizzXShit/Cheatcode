class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort()
        ans=0
        i=0
        j=len(happiness)-1
        while k>i:
            if happiness[j]-i>0:
                ans+=(happiness[j])-i
            
            i+=1
            j-=1
        return ans


