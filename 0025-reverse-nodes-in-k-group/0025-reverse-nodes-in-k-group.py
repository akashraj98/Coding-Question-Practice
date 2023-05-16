# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummyhead = dummy = ListNode(0)
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
            if len(stack) ==k:
                while stack:
                    dummy.next = stack.pop()
                    dummy = dummy.next
        if not stack:
            dummy.next = None
        while stack:
            if len(stack)==1:
                start = stack.pop()
                dummy.next = start
            else:   
                node = stack.pop()
        
        return dummyhead.next
                
        
        # dummyhead =dummy = ListNode(0)
        # prev = None
        # curr = head
        # nxt = curr.next
        # count =0
        # while nxt:
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        #     nxt = nxt.next
        #     count+=1
        #     if count == k:
        #         star = new=prev
        #         while new:
        #             dummy.next = new
        #             dummy = dummy.next
        #             new = new.next
        #         count = 0
        #         prev = None
        # curr.next = prev
        # while curr:
        #     dummy.next = curr
        #     curr = curr.next
        #     dummy = dummy.next
        # return dummyhead.next