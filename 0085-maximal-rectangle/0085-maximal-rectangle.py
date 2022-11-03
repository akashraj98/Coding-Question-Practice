class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxheight(heights):
            maxArea = 0
            stack = [] #(index,height)
            for i,h in enumerate(heights):
                start =i
                while stack and stack[-1][-1]>heights[i]:
                    index,height = stack.pop()
                    maxArea = max(maxArea,height*(i-index))
                    start =index    
                stack.append((start,h))
            for i,h in stack:
                maxArea = max(maxArea,h*(len(heights)-i))
            return maxArea
        
        bar = [0]*len(matrix[0])
        area = 0
        for i in range(len(matrix)):
            # add bar with current row
            curr = matrix[i]
            for j in range(len(matrix[i])):
                if curr[j]=="1":
                    bar[j] +=int(curr[j])
                else:
                    bar[j] = 0
            area = max(area,maxheight(bar))
        return area