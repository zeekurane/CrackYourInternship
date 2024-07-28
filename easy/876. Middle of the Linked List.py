# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tor=head
        rab=head
        while rab is not None and rab.next is not None:
            tor=tor.next
            rab=rab.next.next
        return tor