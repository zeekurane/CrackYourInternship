# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        now=head
        while now:
            l+=1
            now=now.next
        result=now=ListNode(0)
        now.next=head
        l-=n
        while l>0:
            l-=1
            now=now.next
        now.next=now.next.next
        return result.next