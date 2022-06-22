# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morris traversal
        def findPred(curr):
            node = curr.left
            while node.right and node.right!= curr:
                node = node.right
            return node
        res = []
        curr = root
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = findPred(curr)
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    res.append(curr.val)
                    curr = curr.right
                    
        
                
        # # iterative solution
        # res = []
        # stack = [] 
        # curr = root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right

        # Recursive solution
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         res.append(root.val)
        #         inorder(root.right)
        # inorder(root)
        return res

