# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            root.val = self.val = root.val+self.val
            self.bstToGst(root.left)
            return root
#         def dfs(node):
#             if node:
#                 dfs(node.left)
#                 visited.append(node.val)
#                 dfs(node.right)
#         def dfs1(node):
#             if node:
#                 dfs1(node.left)
#                 node.val= next(itervisit)
#                 dfs1(node.right)
#         visited = []
        
#         dfs(root)
#         print(visited)
#         for i in range(len(visited)-2,-1,-1):
#             visited[i] = visited[i] + visited[i+1]
#         itervisit = iter(visited)
#         dfs1(root)
#         return root
            