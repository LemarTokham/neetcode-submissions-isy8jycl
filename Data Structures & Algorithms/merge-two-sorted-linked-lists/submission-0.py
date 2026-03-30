# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                print("hit")
                tail.next = list1 # Add to tail of new list
                list1 = list1.next # Move forward in List1
                tail = tail.next # Move tail forward to point to the most recent node
            elif list2.val < list1.val:
                tail.next = list2 # Add to tail of new list
                list2 = list2.next # Move forward in List2
                tail = tail.next # Move tail forward to point to the most recent node
            else: # They are the same
                print("same")
                tail.next = list1 # Add to tail of new list
                list1 = list1.next # Move forward in List1
                tail = tail.next # Move tail forward to point to the most recent node
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
                