# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:  
                p = curr.left
                while p.right:
                    p = p.right  
                p.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

        # if root:
        #     self.flatten(root.right)
        #     self.flatten(root.left)
        #     root.right = self.prev
        #     root.left = None
        #     self.prev = root
        # return None