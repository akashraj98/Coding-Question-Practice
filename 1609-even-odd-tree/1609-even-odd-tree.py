# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        q = deque([root])
        while q:
            prev_n = TreeNode(0) if level%2==0 else TreeNode(999999)

            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if level%2==0:  # even index
                    if node.val> prev_n.val and node.val%2==1:
                        pass
                    else:
                        return False         
                else:              # odd index
                    if node.val < prev_n.val and node.val%2==0:
                        pass
                    else:
                        return False
                
                prev_n = node
            level+=1
                    
        return True