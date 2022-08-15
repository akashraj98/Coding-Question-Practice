# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root:
            n_target =targetSum - root.val
            if n_target == 0 and root.left is None and root.right is None:
                return True
            return self.hasPathSum(root.left,n_target) or self.hasPathSum(root.right,n_target)
                
        return False#True if targetSum ==0 else False