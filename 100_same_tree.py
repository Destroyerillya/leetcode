from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    stack_p, stack_q = [], []
    curr_p, curr_q = p, q
    while True:
        if curr_p and curr_q:
            stack_p.append(curr_p)
            stack_q.append(curr_q)
            curr_p = curr_p.left
            curr_q = curr_q.left
        elif stack_p and stack_q and not curr_p and not curr_q:
            curr_p = stack_p.pop()
            curr_q = stack_q.pop()
            if curr_p.val != curr_q.val:
                return False
            curr_p = curr_p.right
            curr_q = curr_q.right
        elif stack_p and stack_q and not curr_p and curr_q:
            return False
        elif stack_p and stack_q and curr_p and not curr_q:
            return False
        else:
            break
    return True


p = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
q = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
print(isSameTree(p, q))