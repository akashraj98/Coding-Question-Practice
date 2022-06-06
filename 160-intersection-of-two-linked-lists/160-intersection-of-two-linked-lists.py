# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = self.linklength(headA) # find length
        lenB = self.linklength(headB) 

        nodeA = nodeB = None
        if lenA > lenB:
            diff = lenA-lenB
            nodeA = self.seek(headA,diff)
        elif lenB > lenA:
            diff = lenB-lenA
            nodeB = self.seek(headB,diff)
        A = nodeA if nodeA else headA
        B = nodeB if nodeB else headB

        while A != B:
            A = A.next
            B = B.next
        if not A :
            return None
        else:
            return A
        
    def seek(self,head,length):
        count =0
        node = head
        while node:
            node = node.next
            count+=1
            if length == count:
                break
        return node
        
    def linklength(self,head):
        length = 0
        curr  = head
        while curr:
            curr = curr.next
            length +=1

        return length
