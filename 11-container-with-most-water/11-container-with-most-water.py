class Solution:
    def maxArea(self, height: List[int]) -> int:
        start =0
        end = len(height)-1
        max_area = 0
        while start < end:
            breadth = end-start
            if height[start]> height[end]:
                length = height[end]
                end-=1
            else:
                length = height[start]
                start+=1
            area = length * breadth
            if area > max_area:
                max_area = area
        return max_area
                
            