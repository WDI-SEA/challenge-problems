"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_counter = 1
        current_node = head
        if current_node.next == None:
            node_counter = 0
        else:
            while current_node.next:
                current_node = current_node.next
                node_counter += 1
        index = (node_counter / 2) + 1
        print(index)
        next_counter = 0
        current_node = head
        while next_counter < (index - 1):
            next_counter += 1
            current_node = current_node.next
        return current_node
