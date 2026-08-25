# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, big):
            if not node:
                return 0
            
            # check if good
            is_good = 1 if node.val >= big else 0

            # update max value on this path
            new_big = max(node.val, big)

            return(
                is_good 
                + dfs(node.left, new_big)
                +dfs(node.right, new_big)
            )

        return dfs(root, root.val)