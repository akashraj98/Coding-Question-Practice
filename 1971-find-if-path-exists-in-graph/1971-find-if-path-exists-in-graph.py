class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis = set()
        vis.add(source)
        q =deque([source])
        while q:
            el = q.pop()
            if el == destination: return True
            for edge in edges:
                start,end = edge
                nxt = -1
                if start == el and end not in vis:
                    nxt = end
                    vis.add(nxt)
                    q.appendleft(nxt)
                elif end == el and start not in vis:
                    nxt = start
                    vis.add(nxt)
                    q.appendleft(nxt)
                
        print(vis)
        return False
        # for i in range(n):
        #     if i in vis:
        #         continue
        #     vis.add(i)
        #     count+=1
        #     if count >1: return False
        #     q = deque([i])
        #     while q:
        #         el = q.pop()
        #         for edge in edges:
        #             if edge[0] == el and edge[1] not in vis:
        #                 vis.add(edge[1])
        #                 q.appendleft(edge[1])

#         return True
                    