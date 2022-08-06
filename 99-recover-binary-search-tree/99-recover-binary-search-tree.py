# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(-(2<<31+1))
        # [6,3,4,5,2]
        def dfs(root):
            if root:
                dfs(root.left)
                if not self.first and root.val < self.prev.val:
                    self.first = self.prev
                if self.first and root.val < self.prev.val:
                    self.second = root
                self.prev = root
                    
                # do the business
                dfs(root.right)
        dfs(root)
        self.first.val,self.second.val = self.second.val,self.first.val

        
        
#         curr = []
#         def dfs(root):
#             if root:
#                 dfs(root.left)
#                 curr.append(root.val)
#                 dfs(root.right)
#         dfs(root)
#         curr.sort()
#         self.i= 0
#         def dfs2nd(root):
#             if root:
#                 dfs2nd(root.left)
#                 if root.val != curr[self.i]:
#                     root.val = curr[self.i]
#                 self.i+=1
#                 dfs2nd(root.right)
#         dfs2nd(root)
        

