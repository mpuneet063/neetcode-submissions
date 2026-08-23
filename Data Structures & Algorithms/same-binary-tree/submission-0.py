# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_p = []
        res_q = []
        def dfs(node, res):
            if node is None:
                res.append(None)
                # print(res)
            else:
                res.append(node.val)
                print(res)
                dfs(node.left, res)
                dfs(node.right, res)
            return res

        dfs_p = dfs(p, res_p)
        dfs_q = dfs(q, res_q)

        return dfs_p == dfs_q