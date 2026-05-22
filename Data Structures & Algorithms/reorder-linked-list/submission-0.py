# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = null
        curr = head

        while curr:
            nxt = curr.next
            prev.next = curr
            curr = nxt

            

        
        