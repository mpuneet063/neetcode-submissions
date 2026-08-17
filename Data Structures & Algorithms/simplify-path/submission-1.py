class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        l = [item for item in l if item != '']
        stk = []
        for i in l:
            if i == "..":
                if stk:
                    stk.pop()
            elif i != '' and i != '.':
                stk.append(i)
        return '/' + '/'.join(stk)