class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = set()
        count = 0
        for i in range(n):
            if i in vis:
                continue
            vis.add(i)
            count+=1
            q = deque([i])
            while q:
                el = q.pop()
                for adji in range(n):
                    if isConnected[el][adji] and adji not in vis:
                        vis.add(adji)
                        q.appendleft(adji)
        return count