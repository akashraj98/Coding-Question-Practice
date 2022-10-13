class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]
        for i in range(len(triangle)-1,0,-1):
            for j in range(1,len(triangle[i])):
                sm = min(triangle[i][j] ,triangle[i][j-1])
                triangle[i-1][j-1] += sm
            # print(triangle[i-1])
        return triangle[0][0]