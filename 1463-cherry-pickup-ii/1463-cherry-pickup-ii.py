# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         mem= {}
        
#         def dfs(self,i1,i2,j1,j2):
#             key = tuple([i1,i2,j1,j2])

#             if key in mem: 
#                 return mem[key]
#             if j1== -1 or j2== -1 or j1 == n or j2 == n:
#                 return -float('inf')
#             if i1 ==m and i2==m: return 0
#             # current
#             d1 = self.dfs(i1+1,i2+1,j1-1,j2-1,grid)
#             d2 = self.dfs(i1+1,i2+1,j1-1,j2,grid)
#             d3 = self.dfs(i1+1,i2+1,j1-1,j2+1,grid)
#             d4 = self.dfs(i1+1,i2+1,j1,j2-1,grid)
#             d5 = self.dfs(i1+1,i2+1,j1,j2,grid)
#             d6 = self.dfs(i1+1,i2+1,j1,j2-1,grid)
#             d7 = self.dfs(i1+1,i2+1,j1-1,j2-1,grid)
#             d8 = self.dfs(i1+1,i2+1,j1-1,j2,grid)
#             d9 = self.dfs(i1+1,i2+1,j1-1,j2+1,grid)
#             max_res = max([d1,d2,d3,d4,d5,d6,d7,d8,d9])

#             if i1==i2 and j1==j2:
#                 res = grid[i1][j1]
#             else:
#                 res = grid[i1][j1] + max_res + grid[i2][j2]
#             mem[key] =res
#             return res
#         return max(0,dfs(0,0,0,n-1,grid))
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(grid,i1,j1,i2,j2):
            if (i1,j1,i2,j2) in memo: return memo[(i1,j1,i2,j2)]
            #end cases
            if j1 == n or j2 == n or j1 == -1 or j2 == -1: return -float('inf')
            if i1 == m and i2 == m: return 0

            # 9 different next steps
            d1 = dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2 - 1)
            d2 = dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2)
            d3 = dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2 + 1)
            d4 = dfs(grid,i1 + 1,j1 ,i2 + 1,j2 - 1)
            d5 = dfs(grid,i1 + 1,j1 ,i2 + 1,j2)
            d6 = dfs(grid,i1 + 1,j1 ,i2 + 1,j2 + 1)
            d7 = dfs(grid,i1 + 1,j1 + 1 ,i2 + 1,j2 - 1)
            d8 = dfs(grid,i1 + 1,j1 + 1,i2 + 1,j2)
            d9 = dfs(grid,i1 + 1,j1 + 1,i2 + 1,j2 + 1)
            max_res = max([d1,d2,d3,d4,d5,d6,d7,d8,d9])

            #if two robots step on same place
            if i1 == i2 and j1 == j2:
                res = max_res + grid[i1][j1]
            else:
                res = max_res + grid[i1][j1] + grid[i2][j2]
            memo[(i1,j1,i2,j2)] = res
            return res
        return max(dfs(grid,0,0,0,n - 1), 0)