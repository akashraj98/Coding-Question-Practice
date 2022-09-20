class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for n1,n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        vis =set([source])
        q = deque([source])
        while q:
            node = q.popleft()
            print(node)
            if node == destination:
                return True
            for adj in neighbors[node]:
                if adj not in vis:
                    q.append(adj)
                    vis.add(adj)
        return False
            

        
#         if n-1 ==0: #Corner case
#             return True
#         vis = set()
#         # This solution is valid but will give memory exceed for larger case
#         node_no = 1+max([l1[0] for l1 in edges]+ [l1[1] for l1 in edges])
#         adjmatrix = [[0]*node_no for _ in range(node_no)]
#         for i,j in edges:
#             adjmatrix[i][j] = adjmatrix[j][i] = 1
#         vis.add(source)
#         q = deque([source])
#         while q:
#             node=q.popleft()
#             if node == destination:
#                 return True
#             for adj in range(node_no):
#                 if adjmatrix[node][adj] and adj not in vis:
#                     q.append(adj)
#                     vis.add(adj)

#         return False
                    