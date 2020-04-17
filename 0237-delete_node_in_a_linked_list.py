## Just move the next node val to current node and the next pointer from the next node
## no need to shift over all the other elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#The linked list will have at least two elements.
#All of the nodes' values will be unique.
#The given node will not be the tail and it will always be a valid node of the linked list.
#Do not return anything from your function.

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next #this only works because we are guaranteed not to be given tail
