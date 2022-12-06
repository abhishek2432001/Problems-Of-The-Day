''' Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity 


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def oddEvenList(head):
    oddHead = ListNode(None)
    evenHead = ListNode(None)
    oddNode = oddHead
    evenNode = evenHead
    isEven = True
    while head != None:
        if isEven: 
            isEven = False
            oddNode.next = head
            oddNode = oddNode.next
        else:
            isEven = True
            evenNode.next = head
            evenNode = evenNode.next
        head = head.next

    oddNode.next = evenHead.next
    evenNode.next = None
    return oddHead.next