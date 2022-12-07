'''Given a BST and an integer K. Find the Kth Smallest element in the BST using O(1) extra space. 
	  2
    /   \
   1     3
K = 2
Output: 2
Explanation: 2 is the 2nd smallest element in the BST'''


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
def KthSmallestElement(self, root, K): 
    n = 0
    stack = []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left
        curr = stack.pop() 
        n+=1
        if n==K:
            return curr.data
        curr=curr.right
    return -1  