# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# My solution
# space better than 99.48
# time 72 ms 55.09%
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = str(self.rec(l1,1) + self.rec(l2,1))
        a = ListNode(num[len(num)-1])
        cur = a
        for i in range(len(num)-2,-1,-1):
            cur.next = ListNode(num[i])
            cur = cur.next
        return a
    def rec(self,el,i):
        if not el.next:
            return el.val*i
        return el.val*i + self.rec(el.next,i*10)

# Solution from solution with O(max(m,n))  time and space   
# time 76 ms  
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         head = ListNode(0)
#         curr = head
#         c = 0
#         while(l1 or l2):
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0
#             s = x+y+c
#             c = s//10
#             curr.next = ListNode(s%10)
#             curr = curr.next
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
#         if c>0:
#             curr.next = ListNode(c)
#         return head.next
        