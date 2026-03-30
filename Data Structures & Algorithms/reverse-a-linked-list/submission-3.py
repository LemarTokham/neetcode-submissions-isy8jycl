# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = None
        prev_node = dummy_node
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = temp
        return prev_node
