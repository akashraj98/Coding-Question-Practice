# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow =fast = head
        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        # slow =fast = head
        # while fast and fast.next:
        #     slow =slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         slow
        # if fast is None: return None
        # # 12/17 test cases pass 
        # slow = head
        # while slow!=fast:
        #     slow = slow.next
        #     fast = fast.next

        # return slow