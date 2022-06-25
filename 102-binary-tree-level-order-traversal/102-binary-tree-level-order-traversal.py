# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        q = [root]
        res =[]
        while q:
            subl = []
            nextlvl = []
            for i in range(len(q)):
                node=q.pop(0)
                subl.append(node.val)
                if node.left:
                    nextlvl.append(node.left)
                if node.right:
                    nextlvl.append(node.right)
            res.append(subl)
            q = nextlvl
                    
            
        return res