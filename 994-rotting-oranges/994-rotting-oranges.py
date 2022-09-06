class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfshelper(i,j,grid,q,t):
            if i<0 or j<0 or i >= len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
                return
            grid[i][j]=2
            q.appendleft((i,j,t+1))
            self.f_c-=1
            return self.f_c

        m, n = len(grid), len(grid[0])
        self.f_c= 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.f_c +=1
                elif grid[i][j] == 2:
                    q.appendleft((i,j,0))
        if self.f_c==0: return 0
        while q:
            a,b,t = q.pop()
            bfshelper(a-1,b,grid,q,t) 
            bfshelper(a+1,b,grid,q,t)
            bfshelper(a,b+1,grid,q,t)
            bfshelper(a,b-1,grid,q,t)
            
        if self.f_c>0: return -1
        return t

            