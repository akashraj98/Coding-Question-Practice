# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        dummy = node = TreeNode(res[0])
        for i in res[1:]:
            node.right = TreeNode(i)
            node = node.right
                
        return dummy