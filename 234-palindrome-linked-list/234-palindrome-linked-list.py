# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node =curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        
        for i in range(len(stack)//2):
            last = stack.pop()
            if last.val == node.val:
                node= node.next
            else:
                return False
        return True
        
            
        
        