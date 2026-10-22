class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheap=prices[0]
        maxi=0

        for n in prices:
            if n< cheap:
                cheap=n
            p=n-cheap

            if p>maxi:
                maxi=p
        return maxi 


        