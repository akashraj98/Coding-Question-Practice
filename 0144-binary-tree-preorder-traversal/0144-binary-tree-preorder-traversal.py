# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Moris traversal
        def findPred(curr):
            node = curr.left
            while node.right and node.right!= curr:
                node = node.right
            return node
            
        curr =root
        res = []
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = findPred(curr)
                if pred.right is None:
                    pred.right = curr
                    res.append(curr.val)
                    curr = curr.left
                else:
                    pred.right = None
                    curr = curr.right
        return res
        
#         res = []
#         def preorder(root):
#             if root:
#                 res.append(root.val)
#                 preorder(root.left)
#                 preorder(root.right)                
                
#         preorder(root)
#         return res
                