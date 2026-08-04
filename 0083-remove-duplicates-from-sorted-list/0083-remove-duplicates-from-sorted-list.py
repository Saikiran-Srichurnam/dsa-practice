# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        
        prev = head
        curr = head.next

        while curr is not None:
            if curr.val != prev.val:
                prev = curr
            else:
                prev.next = curr.next
            
            curr = curr.next
        
        return head