# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head

        prev = dummy
        cur = dummy.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:  ## this condition is necessary in case we have more than one node in a row with node.val == val
                prev = cur
            cur = cur.next

        return dummy.next