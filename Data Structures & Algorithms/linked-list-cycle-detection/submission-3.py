# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        counter = 0

        while cur:
            print(cur.val)
            counter +=1

            if counter > 100:
                return True
            elif not cur.next:
                return False
                
            cur =  cur.next
        return False


            

        
        