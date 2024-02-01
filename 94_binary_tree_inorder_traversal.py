from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    if root:
        res += inorderTraversal(root.left)
        res.append(root.val)
        res += inorderTraversal(root.right)
    return res



root = TreeNode(2, TreeNode(1), TreeNode(3))

print(inorderTraversal(root))
