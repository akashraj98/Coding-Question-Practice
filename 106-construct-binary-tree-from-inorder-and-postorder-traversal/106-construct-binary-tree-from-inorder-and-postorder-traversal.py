# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inodx = {elem:i for i,elem in enumerate(inorder)}
        def f(postEnd,postStart,InStart,InEnd):
            node_val =postorder[postEnd]
            indx =inodx[node_val]
            node = TreeNode(node_val)
            l= indx-InStart
            r=InEnd-indx
            node.left = f(postEnd-1-r,postStart,InStart,indx-1) if l else None
            node.right = f(postEnd-1,postEnd-r,indx+1,InEnd) if r else None
            return node
        return f(len(postorder)-1,0,0,len(inorder)-1)
        