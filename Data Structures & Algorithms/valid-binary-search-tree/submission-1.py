# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q=deque([(root,float("-inf"),float("inf"))])
        while q:
            node,left,right=q.popleft()
            if not(left<node.val<right):
                return False
            if node.left:
                q.append((node.left,left,node.val))
            if node.right:
                q.append((node.right,node.val,right))
        return True