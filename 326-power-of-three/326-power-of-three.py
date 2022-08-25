import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(n):
            j= 3**i
            if n==j:
                return True
            elif j>n:
                return False