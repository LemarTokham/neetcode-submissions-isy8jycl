# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        list_len = 0
        while curr:
            list_len += 1
            curr = curr.next

        if list_len < 2:
            return None
        
        curr = head
        iterations = 0
        prev_node = None
        while curr: # We want to make a new reversed list of the second half
            if iterations >= list_len//2:
                prev_node.next = None
                list2 = self.reverseList(curr)
                break
            prev_node = curr
            curr = curr.next
            iterations += 1
        
        # Now we join both lists
        list1 = head
        # list2 has already been made from above
        dummy_node = None
        node = list2
        list1
        while list1 and list2: # All that is left is to merge both lists
            if node == list2:
                temp = list1.next
                if not node:
                    break
                list1.next = node
                list1 = temp
                node = list1
            if node == list1:
                temp = list2.next
                if not node:
                    break
                list2.next = node
                list2 = temp
                node = list2
            if not node:
                break

        
        return list1
                
            

            


        
    def reverseList(self, head):
        # Returns a head of a new list
        dummy_node = None
        prev_node = dummy_node
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = temp
        return prev_node