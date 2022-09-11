# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mid val
        start =slow = fast = head
        count = 0
        while fast and fast.next:
            count+=1
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        #end = prev
        for i in range(count):
            if start.val == prev.val:
                start=start.next
                prev = prev.next
            else:
                return False
        return True
            
        
        