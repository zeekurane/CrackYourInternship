# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans=0
        num_of_nodes=0
        s=""
        while head:
            s+=str(head.val)
            num_of_nodes+=1
            head=head.next
        for num in s:
            if num=="1":
                ans+=(int(num)*2)**(num_of_nodes-1)
            num_of_nodes-=1
            
        return ans