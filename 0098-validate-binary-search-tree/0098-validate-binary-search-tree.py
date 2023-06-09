# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def validate(self,root,low,high):
        if not root:
            return True
        if not(low<root.val and root.val < high):
                return False
        return(
            self.validate(root.left,low,root.val)
            and self.validate(root.right,root.val,high))
    
    def isValidBST(self, root):
        left = float("-inf")
        right = float("+inf")
        return self.validate(root,left,right)
        