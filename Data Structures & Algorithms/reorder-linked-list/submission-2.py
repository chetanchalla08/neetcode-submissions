# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next
        
        left = 0
        right = len(nodes) - 1
        
        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left == right:
                break
            
            nodes[right].next = nodes[left]
            right -= 1

        if nodes:
            nodes[left].next = None
