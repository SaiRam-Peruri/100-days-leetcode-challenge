class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumprice=prices[0]
        maxprofit=0

        for price in prices[1:]:
            maxprofit=max(maxprofit,price-minimumprice)
            minimumprice=min(minimumprice,price)
        return maxprofit