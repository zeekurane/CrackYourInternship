# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1=headA
        h2=headB
        len1=0
        len2=0
        while h1:
            len1+=1
            h1=h1.next
        while h2:
            len2+=1
            h2=h2.next
        h1=headA
        h2=headB
        if len1<len2:
            for _ in range(abs(len1-len2)):
                h2=h2.next
        else:
            for _ in range(abs(len1-len2)):
                h1=h1.next
        while h1!=h2:
            h1=h1.next
            h2=h2.next
        return h1