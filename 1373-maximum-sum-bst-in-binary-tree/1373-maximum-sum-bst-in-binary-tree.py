# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.msum = 0
        def f(root):
            if not root:
                return float("inf"),float("-inf"),0
            lmin,lmax,lsum = f(root.left)
            rmin,rmax,rsum = f(root.right)
            
            if lmax< root.val < rmin:
                #merge/valid 
                currsum = lsum + root.val + rsum
                self.msum = max(self.msum,currsum)
                return min(lmin,root.val),max(rmax,root.val),currsum
            
            return float("-inf"),float("inf"),0
        
        f(root)
        return self.msum