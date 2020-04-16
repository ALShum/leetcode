## Add element by element and track overflow when element > 9

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans_head = ListNode(None)
        n_ptr = ans_head

        overflow = 0
        while l1 and l2:
            s = l1.val + l2.val + overflow
            overflow = 0

            if s > 9:
                overflow += 1
                s -= 10
            new_node = ListNode(s)
            n_ptr.next = new_node
            l1 = l1.next
            l2 = l2.next
            n_ptr = n_ptr.next

        while l1:
            s = l1.val + overflow
            overflow = 0

            if s > 9:
                overflow += 1
                s -= 10
            new_node = ListNode(s)
            l1 = l1.next
            n_ptr.next = new_node
            n_ptr = n_ptr.next

        while l2:
            s = l2.val + overflow
            overflow = 0

            if s > 9:
                overflow += 1
                s -= 10
            new_node = ListNode(s)
            l2 = l2.next
            n_ptr.next = new_node
            n_ptr = n_ptr.next

        if overflow > 0:
            new_node = ListNode(overflow)
            n_ptr.next = new_node
            n_ptr = n_ptr.next

        return ans_head.next
