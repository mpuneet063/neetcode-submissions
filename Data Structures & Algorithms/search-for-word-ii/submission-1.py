class Node:
    def __init__(self):
        self.children = [None]*26
        self.refs = 0
        self.idx = -1


    def insert(self, word: str, i) -> None:
        cur = self
        cur.refs += 1
        for w in word:
            index = ord(w) - ord('a')
            if not cur.children[index]:
                cur.children[index] = Node()
                
            cur = cur.children[index]
            cur.refs += 1
        cur.idx = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        n, m = len(board), len(board[0])
        for w in range(len(words)):
            root.insert(words[w], w)
        res = []

        def getIndex(c):
            idx = ord(c) - ord('a')
            return idx

        def dfs(r,c,node):

            if (r <0 or r>=n or c<0 or c>=m or board[r][c] == '*' or not node.children[getIndex(board[r][c])]):
                return 0
            

            ch = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[getIndex(ch)]
            found = 0

            if node.idx != -1: #found a word
                res.append(words[node.idx])
                node.idx = -1
                found += 1

            found += dfs(r-1,c,node)
            found += dfs(r+1,c,node)
            found += dfs(r,c-1,node)
            found += dfs(r,c+1,node)

            board[r][c] = ch
            node.refs -= found

            if node.refs == 0:
                # prune
                prev.children[getIndex(ch)] = None
            
            
            return found

        for r in range(n):
            for c in range(m):
                count = dfs(r,c,root)
                root.refs -= count

        return res