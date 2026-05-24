# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len, tail = 0, head
        while tail:
            tail = tail.next
            len+=1
        if len == 1:
            return None    
        index = len-n-1
        dummy = head
        while index>0:
            dummy = dummy.next
            index -=1  

       

        nxt = dummy.next.next
        dummy.next = nxt
        return head

