"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Create a mapping between original nodes and copied nodes
        node_map = {}

        # Create copies of nodes and populate the mapping
        dummy = Node(0)
        current = dummy
        original = head

        while original:
            new_node = Node(original.val)
            node_map[original] = new_node
            current.next = new_node

            current = current.next
            original = original.next

        # Update the random pointers using the mapping
        current = dummy.next
        original = head

        while original:
            if original.random:
                current.random = node_map[original.random]
            original = original.next
            current = current.next

        return dummy.next