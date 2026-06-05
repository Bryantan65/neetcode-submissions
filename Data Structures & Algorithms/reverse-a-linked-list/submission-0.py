# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            temp = cur.next #hold next to traverse
            cur.next = None #disconnect

            cur.next = prev
            prev = cur #hold prev
            cur = temp
        return prev

            