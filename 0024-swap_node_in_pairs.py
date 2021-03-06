## Just use recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first = head
        second = head.next
        rest = head.next.next

        second.next = first
        first.next = self.swapPairs(rest)
        return second

