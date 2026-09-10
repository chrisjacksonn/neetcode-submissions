# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        # while curr is not null
        while curr: 
            # make sure we don't lose the next one
            temp = curr.next

            # update the next one to become the prev
            curr.next = prev

            prev = curr

            curr = temp

        return prev



        