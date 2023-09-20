class Solution:
    def mySqrt(self, x: int) -> int:
        # Nive approach Idea is to do square from start to end and 
        # keep calculating square and stop when sqr is greater than x
        # return the prev i as we are rounding down
        # i=1
        # while i*i <= x:
        #     i+=1
        # return i-1
        low,high = 1,x
        while low<=high:
            mid = (high+low)//2
            if mid*mid <x:
                low = mid+1
            elif mid*mid >x:
                high = mid-1
            else:
                return mid

        return high
        
    