class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j,start_c):
            print(i,j)
            if i<0 or j< 0 or i >= len(image) or j >=len(image[0]) or image[i][j] != start_c:
                return 
            image[i][j] = color
            dfs(i+1,j,start_c)
            dfs(i-1,j,start_c)
            dfs(i,j+1,start_c)
            dfs(i,j-1,start_c)
        start_c = image[sr][sc]
        if start_c == color: return image
        dfs(sr,sc,start_c)
        return image