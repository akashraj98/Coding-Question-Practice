class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Find first island
        # Convert it to 2s and push it in queue
    
        n = len(grid)
        f_x,f_y = 0,0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    f_x,f_y = i,j
                    break
        def inrange(cur_x,cur_y):
            return 0 <= cur_x < n and 0 <= cur_y < n
        def nextfour(x,y):
            return [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            
        def dfs(x,y):
            grid[x][y]=2
            bfs_queue.append((x,y))
            for cur_x,cur_y in nextfour(x,y):
                if inrange(cur_x,cur_y) and grid[cur_x][cur_y] == 1:
                    dfs(cur_x, cur_y)
        bfs_queue = []
        dfs(f_x,f_y)
        distance = 0
        while bfs_queue:
            new_bfs=[]
            for x,y in bfs_queue:
                for cur_x,cur_y in nextfour(x,y):
                    if inrange(cur_x,cur_y):
                        if grid[cur_x][cur_y] ==1:
                            return distance
                        elif grid[cur_x][cur_y]==0:
                            new_bfs.append((cur_x,cur_y))
                            grid[cur_x][cur_y]=-1
                            
            bfs_queue = new_bfs
            distance +=1       