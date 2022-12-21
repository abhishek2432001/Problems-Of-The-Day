'''Given a linked list of N nodes, sorted in ascending order based on the absolute values of its data,i.e. negative values are considered as positive ones. Sort the linked list in ascending order according to the actual values, and consider negative numbers as negative and positive numbers as positive.


Example 1:

Input: 
List: 1, -2, -3, 4, -5
Output: 
List: -5, -3, -2, 1, 4
Explanation: 
Actual sorted order of {1, -2, -3, 4, -5}
is {-5, -3, -2, 1, 4}
 

Example 2:

Input: 
List: 5, -10
Output: 
List: -10, 5
Explanation:
Actual sorted order of {5, -10}
is {5, 10}
'''
#User function Template for python3

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    
    def sortList(self,head):
        pos = pos_head = Node(0)
        neg = neg_tail = Node(0)
        while head:
            if head.data >= 0:
                pos.next = head
                pos = head
                head = head.next
            else:
                if neg == neg_tail:
                    neg_tail = head
                temp = head.next
                head.next = neg.next
                neg.next = head
                head = temp
        pos.next = None
        neg_tail.next = pos_head.next
        return neg.next


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.last=self.head

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.last=new_node
            return
        self.last.next=new_node
        self.last=self.last.next
        

    
def PrintList(head):
    while head:
        print(head.data,end=' ')
        head=head.next