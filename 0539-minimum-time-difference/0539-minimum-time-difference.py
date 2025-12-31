class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        k=[]
        minn=float('inf')
        for i in timePoints:
            k.append((int(i[0])*10*60)+(int(i[1])*60)+(int(i[3])*10)+(int(i[4])))
        
        # for i in range(len(k)):
        #     for j in range(len(k)):
        #         if i!=j:
        #             a=k[i]
        #             b=k[j]
        #             if b<720 and a>720:
        #                 ans= min(a-(720+b),b+1440-a)
        #             elif b>720 and a<720:
        #                 ans=min(a+1440-b,b-(720+a))
        #             else:
        #                 ans=(max(a,b))-(min(a,b))
        #             if ans<minn:
        #                 minn=ans
        k.sort()
        for i in range(1, len(k)): 
            minn = min(minn, k[i] - k[i-1]) 
        minn = min(minn, 1440 - (k[-1] - k[0]))
        return minn
                        
                    
        