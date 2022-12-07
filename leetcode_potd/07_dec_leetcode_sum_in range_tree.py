'''Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def rangeSumBST(root, l, r) :
    if(root is None or l>r):
        return 0
    if(root.val<l):
        return rangeSumBST(root.right, l, r)
    if(root.val>r):
        return rangeSumBST(root.left, l, r)
    return root.val + rangeSumBST(root.left, l, r) + rangeSumBST(root.right, l, r)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.right = TreeNode(18)
root.left.right = TreeNode(7)
root.left.left = TreeNode(3)
print(rangeSumBST(root,7,15))