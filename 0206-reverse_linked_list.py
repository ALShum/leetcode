## For recursion use head.next.next instead of n.next
## because n will be the last element in the original list that gets returned

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        cur = head

        while cur:
            rest = cur.next
            cur.next = prev
            prev = cur
            cur = rest
        return prev

    def reverseList(self, head):
        if not head or not head.next:
            return head

        n = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return n
