## Just iterate the node with the smaller value each time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy
        while l1 and l2:
            val = l1.val if l1.val < l2.val else l2.val
            cur.next = ListNode(val)
            cur = cur.next
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next

