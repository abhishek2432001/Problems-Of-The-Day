'''872. Leaf-Similar Trees
Consider all the leaves of a binary tree, from left to right order, 
the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.'''


def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leave1 = []
        leave2 = []
        self.dfs(root1,leave1)
        self.dfs(root2,leave2)
        return leave1 == leave2
def dfs(self,root,leaves = []):
    if root is None:
        return

    # Checking Leaf node
    if root.left is None and root.right is None:
        leaves.append(root.val)
    self.dfs(root.left,leaves)
    self.dfs(root.right,leaves)