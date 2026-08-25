# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        while head:
            if (head.val in sett) and head.next:
                return True
            sett.add(head.val)
            head = head.next
        
        return False