# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=op=ListNode(0)
        c=0
        while l1 or l2 or c==1:
            if l1:
                d1=l1.val
            else:
                d1=0
            if l2:
                d2=l2.val
            else:
                d2=0
            new=ListNode((d1+d2+c)%10)
            c=(d1+d2+c)//10
            op.next=new
            op=op.next
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return result.next