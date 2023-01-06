class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        available = coins
        res=0
        for cost in costs:
            if cost> available:
                break
            available-=cost
            res+=1
        return res