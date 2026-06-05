# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        cur = head
        prev = None

        while cur:
            val.append(cur.val)
            cur = cur.next
        
        print(val)
        cur = head
        
        while cur:
            temp = cur.next  #temp node that saves the next 0 > 1 (temp)
            cur.next = prev #  pointer to 1 becomes 0 reversed
            prev = cur #move prev forward?

            cur = temp # move to the next
            
        cur = prev
        
        while cur:
            val.append(cur.val)
            cur = cur.next
        print(val)

        

        # cur = head
        # prev = None
        return prev

       
            