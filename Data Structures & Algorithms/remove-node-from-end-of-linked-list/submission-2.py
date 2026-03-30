# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find len of list
        k = 0
        curr = head
        while curr:
            k += 1
            curr = curr.next
        if k == 1 and n < 2:
            return None

        rmv_index = k - n # When iteration match this varaible we remove the node we are on
        curr = head
        count = 0
        dummy = ListNode(0)
        prev = dummy
        while curr:
            print(count, curr.val)
            if count == rmv_index: # Remove the node
                print(count, rmv_index, curr.val, prev.val)
                temp = curr.next
                prev.next = temp
                curr.next = None
                if not count: # count = 0
                    head = temp
                break
            # Move through the list
            temp = curr
            curr = curr.next
            prev = temp
            print(prev)
            count += 1

        return head

        