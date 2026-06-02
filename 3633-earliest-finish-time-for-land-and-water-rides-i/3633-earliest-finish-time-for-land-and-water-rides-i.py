class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        # """
        # :type landStartTime: List[int]
        # :type landDuration: List[int]
        # :type waterStartTime: List[int]
        # :type waterDuration: List[int]
        # :rtype: int
        # """
        # tt=0
        # ls=0
        # ws=0
    
        # if landStartTime[ls]<waterStartTime[ws]:
        #     tt+=landStartTime[ls]
        #     tt+=landDuration[ls]
        #     if tt<waterStartTime[ws]:
        #         tt+=waterStartTime[ws]-(landStartTime[ls]+landDuration[ls])
        #     tt+=waterDuration[ws]
        # if waterStartTime[ws]<landStartTime[ls]:
        #     tt+=waterStartTime[ws]
        #     tt+=waterDuration[ws]
        #     if tt<landStartTime[ls]:
        #         tt+=landStartTime[ls]-(waterStartTime[ws]+waterDuration[ws])
        #     tt+=landDuration[ls]
        # return tt

        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                land_finish = landStartTime[i] + landDuration[i]
                finish1 = max(land_finish, waterStartTime[j]) + waterDuration[j]

                water_finish = waterStartTime[j] + waterDuration[j]
                finish2 = max(water_finish, landStartTime[i]) + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans

