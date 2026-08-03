# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        left = dummy
        right = dummy
        counter = 0
        while counter != n:
            right = right.next
            counter += 1
        
        while right is not None:
            if right.next is None:
                left.next = left.next.next
            
            left = left.next
            right = right.next
        
        return dummy.next