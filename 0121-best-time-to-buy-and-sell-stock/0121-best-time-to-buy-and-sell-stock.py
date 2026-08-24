class Solution(object):
    def maxProfit(self, prices):
        cheapest = prices[0]
        maxi = 0

        for price in prices:
            if price < cheapest:
                cheapest = price

            profit = price - cheapest

            if profit > maxi:
                maxi = profit

        return maxi