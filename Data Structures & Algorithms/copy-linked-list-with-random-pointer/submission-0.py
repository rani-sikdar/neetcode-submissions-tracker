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

        # Original node -> Copied node
        copies = {}

        # First pass: create copy of each node
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: connect next and random pointers
        curr = head
        while curr:
            copies[curr].next = copies.get(curr.next)
            copies[curr].random = copies.get(curr.random)
            curr = curr.next

        return copies[head]
