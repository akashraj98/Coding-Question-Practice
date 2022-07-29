# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def f(isleft,depth,root):
            if root:
                if isleft:
                    return max(f(1,1,root.left),f(0,depth+1,root.right))
                else:
                    return max(f(1,depth+1,root.left),f(0,1,root.right))
            else: 
                return depth-1

            
        return f(0,0,root)

        
        
        
        