## don't update prev = cur if we deleted a node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head

        prev = dummy
        cur = head
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head