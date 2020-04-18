## Use a minheap
## Convert list of nodes into list of tuples: (value, index, node)
## 1. The tricky part is the comparator for tuple, if the first element is equal it uses the second
## Because the node doesn't implement '<' or '>' we need the index in the tuple
## 2. Make sure you reinsert nodes after they're popped out of the heap, check if next node exists
## 3. Becareful about degenerate cases: [], [[]], [[], []] etc

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [(l.val,i,l) for i,l in enumerate(lists) if l]
        if not lists:
            return None

        heapq.heapify(lists)
        _, idx, head_node = heapq.heappop(lists)
        if head_node.next:
            val = head_node.next.val
            heapq.heappush(lists, (val, idx, head_node.next))
        prev_node = head_node
        print(lists)
        while lists:
            _, idx, next_node = heapq.heappop(lists)
            if next_node.next:
                val = next_node.next.val
                heapq.heappush(lists, (val, idx, next_node.next))
            prev_node.next = next_node
            prev_node = next_node

        prev_node.next = None
        return head_node
