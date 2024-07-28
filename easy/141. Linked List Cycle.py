# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen=set()
        now=head
        while now:
            if now in seen:
                return True
            seen.add(now)
            now=now.next
        return False