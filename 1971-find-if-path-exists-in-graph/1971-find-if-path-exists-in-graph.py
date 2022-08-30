class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis = set()
        adjnode = defaultdict(list)
        for edge in edges:
            adjnode[edge[0]].append(edge[1])
            adjnode[edge[1]].append(edge[0])
        
        vis.add(source)
        q = deque([source])
        while q:
            node=q.popleft()
            if node == destination: return True
            for adj in adjnode[node]:
                if adj not in vis:
                    q.append(adj)
                    vis.add(adj)
        return False
                    