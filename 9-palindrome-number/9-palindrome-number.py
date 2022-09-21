class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_s=str(x)
        return  x_s == x_s[::-1]
        