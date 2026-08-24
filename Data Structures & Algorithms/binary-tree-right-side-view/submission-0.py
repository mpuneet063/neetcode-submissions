# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            
            res = []
            q = collections.deque()
            q.append(root)

            while q:
                qLen = len(q)
                level = []
                for i in range(qLen):
                    node = q.popleft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                if level:

                    res.append(level)

            return res

        bfs = levelOrder(root)
        res = []
        for b in bfs:
            res.append(b[-1])

        return res