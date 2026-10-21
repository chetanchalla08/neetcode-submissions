# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            digit1 = 0
            digit2 = 0

            if l1:
                digit1 = l1.val
                l1 = l1.next

            if l2:
                digit2 = l2.val
                l2 = l2.next

            total = digit1 + digit2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next
