class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        l_max = 0
        r_max = 0
        area = 0
        while left < right:
            if height[left] <= height[right]:  # since right bar is greater so 
                if height[left] >= l_max:     # the water level in b/w is deter mine by left bar which is small
                    l_max = height[left]
                else:
                    area+= l_max - height[left]
                left+=1
            else:                         #since left bar is greater so water 
                if height[right] >= r_max:# level is determine by right bar which is smaller
                    r_max = height[right]  #for curr position  if r_bar is greater than max right bar till now then no water can be filler 
                                           # else water can be filled in curr positon with level max_r - height[r_bar]
                else:
                    area += r_max - height[right]
                right-=1

        return area