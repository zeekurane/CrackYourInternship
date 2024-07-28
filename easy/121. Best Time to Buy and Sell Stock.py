class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices=[0 for _ in range(len(prices))]
        max_num=0
        min_num=10001
        diff=0
        for i in range(-1,-len(prices)-1,-1):
            if max_num<prices[i]:
                max_num=prices[i]
            max_prices[i]=max_num
        for i in range(len(prices)):
            if min_num>prices[i]:
                min_num=prices[i]
            if diff<max_prices[i]-min_num:
                diff=max_prices[i]-min_num
        return diff