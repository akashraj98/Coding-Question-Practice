class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]
        res = triangle[-1]
        for i in range(len(triangle)-1,0,-1):
            for j in range(1,len(triangle[i])):
                res[j-1] = min(res[j],res[j-1])+ triangle[i-1][j-1]
        return res[0]
#                 sm = min(triangle[i][j] ,triangle[i][j-1])
#                 triangle[i-1][j-1] += sm

#         return triangle[0][0]
