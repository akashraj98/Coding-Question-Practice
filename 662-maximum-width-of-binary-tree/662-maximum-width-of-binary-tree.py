# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        q = deque([(root,0)])
        width = 0
        while q:
            width = max(width,q[-1][1]- q[0][1] +1)
            temp = []
            for node,i in q:
                if node.left:
                    temp.append((node.left,2*i+1))
                if node.right:
                    temp.append((node.right,2*i+2))
            q = temp
                
        return width

            