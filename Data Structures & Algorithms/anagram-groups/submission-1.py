class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Defining a dictionary with values as a list

        for s in strs:
            count = [0]*26  # make a list of 26 integers 

            for c in s:
                count[ord(c) - ord('a')] += 1   # increase the count of letters that occur

            res[tuple(count)].append(s) # populate the hashmap

        return list(res.values())