# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #we can use a dummy node 
        # and prev pointer to remove last node if it is duplicate frm our dummy list
        # if dummynodeval == currnode val: seek till they are different
        # remove end from dummy list by using prev pointer
        # append the node with different value (it will be none if we have duplicate in end)
        # repeat till end of linked list
        
        curr = head.next
        dummy = dummyNode = ListNode(0,head)
        prev  = dummy
        dummy = dummy.next
        
        while curr:
            if dummy.val != curr.val:
                dummy.next = curr
                prev = dummy
                dummy = dummy.next
                curr = curr.next
            else:
                #We found duplicate node
                while curr and curr.val== dummy.val:
                    curr = curr.next
                prev.next = curr
                dummy = prev.next
                if curr:
                    curr = curr.next
        return dummyNode.next
       