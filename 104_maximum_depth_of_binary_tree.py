from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def maxDepth(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    if not root.right:
        return 1 + maxDepth(root.left)
    elif not root.left:
        return 1 + maxDepth(root.right)
    else:
        return max(maxDepth(root.left),  maxDepth(root.right)) + 1


root = TreeNode(val=0, left=TreeNode(val=2, left=TreeNode(val=1, left=TreeNode(val=5), right=TreeNode(val=1))), right=TreeNode(val=4, left=TreeNode(3, right=TreeNode(6)), right=TreeNode(-1, right=TreeNode(8))))
print(maxDepth(root))