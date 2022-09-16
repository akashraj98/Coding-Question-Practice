# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use sentient node(9000)
        # if curr is smaller than sentient add curr in end
        # search curr positin in sentient from sentient head
        # use pointer to insert the node
        # Keep doing this till all node sare sorted
        
        dummyhead = ListNode(-9999,head)
        curr = head.next
        dummy = dummyhead.next
        while curr:
            if curr.val >= dummy.val:
                dummy.next = curr
                dummy = dummy.next
                curr = curr.next
            else:
                t =curr.next
                head = dummyhead
                prev = None
                while head.val < curr.val:
                    prev = head
                    head = head.next
                prev.next = curr
                curr.next = head
                curr = t
        if dummy is not None: 
            dummy.next = None
        return dummyhead.next
        
        