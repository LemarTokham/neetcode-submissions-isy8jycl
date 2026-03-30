# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        curr = dummy
        carry = 0
        while curr1 and curr2:
            res = curr1.val + curr2.val + carry
            str_res = str(res)

            if len(str_res) > 1:
                if curr1.next == None and curr2.next == None:
                    curr.next = ListNode(str_res[1])
                    curr = curr.next
                    curr.next = ListNode(str_res[0])
                    curr1 = curr1.next
                    curr2 = curr2.next
                    continue

                carry = int(str_res[0])
                curr.next = ListNode(str_res[1])
            else:
                carry = 0
                print(str_res)
                curr.next = ListNode(str_res)

            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        if curr1:
            finalCurr = curr1
        finalCurr = curr2
        while curr1:
            res = curr1.val + carry
            print(res)
            str_res = str(res)
            if len(str_res) > 1:
                if curr1.next == None: # add both nums to list
                    curr.next = ListNode(str_res[1])
                    curr = curr.next
                    curr.next = ListNode(str_res[0])
                    break # next is just None so exit early

                carry = int(str_res[0])
                curr.next = ListNode(str_res[1])
            else:
                carry = 0
                curr.next = ListNode(str_res)

    
            curr = curr.next
            curr1 = curr1.next

        while curr2:
            res = curr2.val + carry
            print(res)
            str_res = str(res)
            if len(str_res) > 1:
                print("hit")
                if curr2.next == None: # add both nums to list
                    curr.next = ListNode(str_res[1])
                    curr = curr.next
                    curr.next = ListNode(str_res[0])
                    break # next is just None so exit early

                carry = int(str_res[0])
                curr.next = ListNode(str_res[1])
            else:
                carry = 0
                curr.next = ListNode(str_res)
            curr = curr.next
            curr2 = curr2.next

        return dummy.next
