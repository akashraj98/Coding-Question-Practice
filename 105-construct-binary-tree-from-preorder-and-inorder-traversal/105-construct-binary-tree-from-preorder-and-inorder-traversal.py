# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inodx = {elem:i for i,elem in enumerate(inorder)}
        def f(prStart,prEnd,InStart,InEnd):
            node_val =preorder[prStart]
            indx =inodx[node_val]
            node = TreeNode(node_val)
            l= indx-InStart
            r=InEnd-indx
            node.left = f(prStart+1,prStart+l,InStart,indx-1) if l else None
            node.right = f(prStart+1+l,prEnd,indx+1,InEnd) if r else None
            return node
        return f(0,len(preorder)-1,0,len(inorder)-1)


