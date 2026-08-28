# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def level(root):
            if not root:
                return []
            q = deque()
            q.append(root)
            res = []

            while q:
                qlen = len(q)
                for i in range(qlen):
                    node = q.popleft()
                    if node:
                        res.append(str(node.val))
                        q.append(node.left)
                        q.append(node.right)
                    else:
                        res.append('n')

            return res
        tree = [str(t) for t in level(root)]
        
        return ','.join(tree)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return 

        l = data.split(",")
        root = TreeNode(int(l[0]))
        q = deque()
        q.append(root)
        i = 1

        while q and i < len(l):
            node = q.popleft()

            if l[i] != 'n':
                node.left = TreeNode(int(l[i]))
                q.append(node.left)
            i += 1
            if i < len(l) and l[i] != 'n':
                node.right = TreeNode(int(l[i]))
                q.append(node.right)
            i += 1  
            
        return root