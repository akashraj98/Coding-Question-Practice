# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque([root])
        sm = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if low <= node.val and node.val <= high:
                    sm+= node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return sm
