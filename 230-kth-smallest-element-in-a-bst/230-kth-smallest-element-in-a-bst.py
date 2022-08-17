# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.c = 0
        def dfs(root):
            if root:
                dfs(root.left)
                self.c+=1
                if k== self.c:
                    self.ans = root.val
                    return
                dfs(root.right)
        dfs(root)
        return self.ans