# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case 
        if not head or not head.next or k == 0:
            return head
        
        # find length of the linkedlist
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Number of rotations
        k = k % length

        # if k == 0 no rotations
        if k == 0:
            return head
        
        tail.next = head

        # steps to reach newTail
        steps = length - k - 1
        newTail = head
        for _ in range(steps):
            newTail = newTail.next

        newHead = newTail.next
        newTail.next = None

        return newHead