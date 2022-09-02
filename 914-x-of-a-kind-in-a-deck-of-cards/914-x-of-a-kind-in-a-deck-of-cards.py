class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dp = [[-1 for i in range(1001)] for j in range(1001)]
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return abs(a)
        count = Counter(deck)
        return reduce(gcd,count.values())>=2
