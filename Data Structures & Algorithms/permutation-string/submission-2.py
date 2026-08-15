class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        # build a frequency map for s1
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c,0)
        need = len(count1)  # need stores the total no. of UNIQUE chars in s1 that must have their exact freqs matched in the window

        # start a window at every index 'i' in s2
        for i in range(len(s2)):
            count2, cur = {}, 0     # frequency map for s2, cur to count how many UNIQUE chars have reached the target freq
            for j in range(i, len(s2)):     #expanding the window
                count2[s2[j]] = 1 + count2.get(s2[j], 0)    # inc freq of char in current window
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break   #early pruning if char is not in s1 or its count exceeds the count in s1
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1    # freq matched and incrd
                if cur == need:
                    return True     # if the match is correct, success

        return False