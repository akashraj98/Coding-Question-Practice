class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis = set()
        count = 0
        n = len(isConnected)
        for i in range(n):
            if i in vis:
                continue
            count+=1
            vis.add(i)
            q = deque([i]) # everytime we need to make ques
            #since we will visit all nodes that can be visited from i
            while q:
                el= q.pop()
                for adj in range(n):
                    if isConnected[el][adj]:
                        if adj not in vis:
                            vis.add(adj)
                            q.appendleft(adj)
        return count