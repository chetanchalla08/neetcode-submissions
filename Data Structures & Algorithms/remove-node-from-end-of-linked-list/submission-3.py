# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next
        
        remove_index = len(nodes) - n

        if remove_index == 0:
            return head.next

        nodes[remove_index - 1].next = nodes[remove_index].next

        return head