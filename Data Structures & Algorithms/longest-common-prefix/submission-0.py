class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""    # created an empty string
        for i in range(len(strs[0])):   # for sample, the length of the first string is the bound
            for s in strs:  # iterating over each element in strs
                if i == len(s) or s[i] != strs[0][i]:
                # if index i is at the length of s, we already have our prefix 
                    return res

            res += strs[0][i]

        return res