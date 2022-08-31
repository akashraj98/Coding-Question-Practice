"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return node    # base case
        #Using hashmap to mark visited node and
        #store Nodes aready created so that its neighbour could be added
        # initially a node will have 0 neighbourt in start
        # We implement using BFS
        clone = {node.val:Node(node.val,[])}
        q = deque([node])
        while q:
            el =q.popleft()
            cur_node=clone[el.val]
            for adj in el.neighbors:
                if adj.val not in clone:
                    clone[adj.val] = Node(adj.val,[])
                    q.append(adj)
                cur_node.neighbors.append(clone[adj.val])
        return clone[node.val]
            