# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pt1 = headA
        pt2 = headB
        # concept is if they are same length then they will meet somewhere
        # if they are diff length then they will also colide sometime in feuture as
        # relative positioning of pts will change since len of two arrays are diff
        # due to diff length one wil scan loop faster than other
        while pt1!=pt2:
            pt1 = pt1.next if pt1 else headB
            pt2 = pt2.next if pt2 else headA
        return pt1
        