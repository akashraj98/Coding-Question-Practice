class Solution:
    def concatenatedBinary(self, n: int) -> int:
        b = ""
        for i in range(n):
            b+=bin(i+1)[2:]

        return int(b,2)%(10**9+7)