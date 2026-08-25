# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = head
        while cur_node:
            temp1 = cur_node
            temp2 = cur_node.next
            temp3 = prev_node
            cur_node.next = temp3
            cur_node = temp2
            prev_node = temp1
        return prev_node

            
