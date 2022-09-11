# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-pldace instead.
        """
        start = node = head 
        stack = []
        while start:
            stack.append(start)
            start = start.next
        curr = head
        for i in range(len(stack)//2):
            node =stack.pop()
            t = curr.next
            curr.next = node
            node.next = t
            curr = t
        curr.next = None
        return head
        