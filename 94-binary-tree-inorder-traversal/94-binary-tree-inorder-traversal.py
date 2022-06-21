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
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right

            
            
        # Recursive solution
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         res.append(root.val)
        #         inorder(root.right)
        # inorder(root)
        return res

