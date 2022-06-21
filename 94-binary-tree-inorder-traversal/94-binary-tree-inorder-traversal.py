# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [] 
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right


            
            
        # Recursive solution
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         res.append(root.val)
        #         inorder(root.right)
        # inorder(root)
        return res

