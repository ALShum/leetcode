## Start a _before_ linked list and an _after_ linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = ListNode(None)
        after = ListNode(None)

        cur_before = before
        cur_after = after

        node = head
        while node:
            if node.val < x:
                cur_before.next = node
                cur_before = cur_before.next
            else:
                cur_after.next = node
                cur_after = cur_after.next
            node = node.next
        cur_after.next = None
        cur_before.next = after.next
        return before.next

