# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()
        curr = head

        while curr:
            # using node position, not the value
            # so if the position is repeated, we can guarantee it's a repeat
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False
        