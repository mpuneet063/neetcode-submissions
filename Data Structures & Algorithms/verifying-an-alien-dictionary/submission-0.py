class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = {}
        for o in range(len(order)):
            alpha[order[o]] = o
        lex = []
        for w in words:
            n = []
            for c in w:
                n.append(alpha[c])
            lex.append(n)

        return lex == sorted(lex)