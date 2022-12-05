'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Approach: Move fast pointer 2 times and slow pointer 1 time the time when fast reaches last node 
slow will have covered half that is middle node
'''


def middleNode(head):
    slow = head
    fast = head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow