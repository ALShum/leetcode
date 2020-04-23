## Iterate through the linkedlists: when reach the end of LL1, send pointer to LL2
## Similarly, when reach the end of LL2, send pointer to LL1.
## If pointers reach the same node, that's the intersection
## If after looping through each list once and we reach the end, there is no intersection

## Alternatively, just use a hashmap or mark each node with visited = True (additional O(n+m) memory required)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        firstIterA = True
        firstIterB = True

        cur_A = headA
        cur_B = headB
        while (firstIterA or firstIterB) or (cur_A and cur_B):
            if not cur_A and firstIterA:
                cur_A = headB
                firstIterA = False
            if not cur_B and firstIterB:
                cur_B = headA
                firstIterB = False
            if cur_A == cur_B:
                return cur_A
            cur_A = cur_A.next
            cur_B = cur_B.next
        return None
