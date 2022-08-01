# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def mDepth(root,depth=0):
            if root:
                return 1+max(mDepth(root.left,depth),mDepth(root.right,depth))
            return 0

        return mDepth(root)
        # return m_depth

        
        
        
        
        
        
        # if not root:
        #     return 0
        # return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))