class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        def ways(i, amount, coins):
            if amount == 0:
                return 1
            if amount < 0 or i == len(coins):
                return 0
            return ways(i, amount - coins[i], coins) + ways(i+1, amount, coins)
        return ways(0,amount,coins)

        