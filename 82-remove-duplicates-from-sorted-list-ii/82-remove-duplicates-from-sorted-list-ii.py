# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #we can use a dummy node and a flag
        #flag will check weather we have duplicate value
        # if flag then seek till value is different
        # remove end from dummy list
        # change flag to 0
        # append the node with different value (it will be none if we have duplicate in end)
        # repeat till end of linked list
        
        curr = head.next
        dummy = dummyNode = ListNode(0,head)
        prev  = dummy
        dummy = dummy.next
        isdup = False
        while curr:
            if dummy.val != curr.val:
                dummy.next = curr
                prev = dummy
                dummy = dummy.next
                curr = curr.next
            else:
                isdup = True
                while curr and curr.val== dummy.val:
                    curr = curr.next
                if isdup:
                    prev.next = curr
                    dummy = prev.next
                isdup = not isdup
                if curr:
                    curr = curr.next
        return dummyNode.next
       