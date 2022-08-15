# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root,isLeft):
            if root:
                if not root.left and not root.right and isLeft:
                    return root.val
                return dfs(root.left,True)+ dfs(root.right,False)
            return 0
        return dfs(root,False)