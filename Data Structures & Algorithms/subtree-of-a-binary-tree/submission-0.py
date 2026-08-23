# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, res):
            if node is None:
                res.append(None)
            else:
                res.append(node.val)
                dfs(node.left, res)
                dfs(node.right, res)
            return res
        res_root, res_sub = [], []
        dfs_root = dfs(root, res_root)
        dfs_sub = dfs(subRoot, res_sub)

        n = len(dfs_root)
        m = len(dfs_sub)
        if m == 0:
            return True
        if m>n:
            return False
        for i in range(n-m+1):
            if dfs_root[i:i+m] == dfs_sub:
                return True
        return False