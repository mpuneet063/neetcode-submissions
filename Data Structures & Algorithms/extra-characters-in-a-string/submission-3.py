# Solve with Trie
class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self, words):
        self.root = Node()
        for w in words:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]

            cur.isWord = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {len(s):0}     # cache used to store possibilities
        trie = Trie(dictionary).root

        def back(i):
            if i in dp:
                return dp[i]

            res = 1 + back(i+1)     # skip curr char
            curr = trie
            for j in range(i,len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isWord:
                    res =  min(res, back(j+1))
            dp[i] = res
            return res

        return back(0)
        