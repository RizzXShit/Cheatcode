class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         diff=prices[j]-prices[i]
        #         profit=max(profit,diff)
        # return profit

        # a=[]
        # for i in range(len(prices)):
        #     a.insert(max(prices[i],prices[i-1]))

        min_price = float('inf') 
        max_profit = 0 
        for price in prices: 
            if price < min_price: 
                min_price = price 
            elif price - min_price > max_profit: 
                max_profit = price - min_price 
        return max_profit
        


        