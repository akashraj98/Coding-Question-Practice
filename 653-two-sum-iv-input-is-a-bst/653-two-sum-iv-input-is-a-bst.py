# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.dic = set()
        self.ans = False
        def dfs(root):
            if root:
                dfs(root.left)
                if root.val not in self.dic:
                    self.dic.add(k-root.val)
                else:
                    self.ans = True
                dfs(root.right)
        dfs(root)
        return self.ans
        