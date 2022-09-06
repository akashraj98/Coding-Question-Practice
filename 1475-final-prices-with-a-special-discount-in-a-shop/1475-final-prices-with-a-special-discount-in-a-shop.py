class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #max monotonic stack
        stack =[]
        for i,price in enumerate(prices):
            while stack and stack[-1][1] >= price:
                index,val = stack.pop()
                prices[index] = val - price
            stack.append((i,price))
        return prices
                