# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
class Solution:
    def __init__(self):
        # lists start out empty
        self.head = None
        self.tail = None
        # how many nodes exists in the list
        self.size = 0

    def reverseList(self, head):
        prev = None
        current_node = head
        
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            
            current_node = next_node
        
        return prev

one = ListNode(1, None)
two = ListNode(2, None)
three = ListNode(3, None)
four = ListNode(4, None)
five = ListNode(5, None)

head = [one, two, three, four, five]
print(one)
print(two)
print(three)
print(four)
print(five)
test = Solution()

test.reverseList(head)