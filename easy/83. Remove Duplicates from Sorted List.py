# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen=set()
        result=op=head
        past=op
        if op:
            present=past.next
        else:
            return op
        if op.next:
            future=present.next
        else:
            return op
        seen.add(past.val)
        while present:
            if present.val in seen:
                past.next=future
            else:
                seen.add(present.val)
                past=past.next
            present=future
            if future:
                future=future.next
        return result