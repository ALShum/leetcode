## Use two dummy nodes to track even and odd indices

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd = ListNode(None)
        even = ListNode(None)

        cur = head
        cur_odd = odd
        cur_even = even
        count = 1
        while cur:
            if count % 2 == 0:
                cur_even.next = cur
                cur_even = cur_even.next
            else:
                cur_odd.next = cur
                cur_odd = cur_odd.next
            cur = cur.next
            count+=1

        cur_even.next = None
        cur_odd.next = even.next
        return odd.next