# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        while l1:
            n1=n1*10+l1.val
            l1=l1.next
        n2=0
        while l2:
            n2=n2*10+l2.val
            l2=l2.next
        s=str(n1+n2)
        ans=node=ListNode(-1)
        for num in s:
            node.next=ListNode(int(num))
            node=node.next
        return ans.next