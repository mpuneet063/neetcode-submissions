class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # nums = set(nums)
        # starters = []
        # for n  in nums:
        #     if n-1 not in nums:
        #         starters.append(n)
        # counts = []
        # for s in starters:
        #     c = s
        #     count = 1
        #     while c in nums:
        #         if c + 1 in nums:
        #             count += 1
        #         c += 1
        #     counts.append(count)

        # return max(counts)

        nums = set(nums)
        longest = 0
        for n in nums:
            # check for starters
            if n-1 not in nums:
                length = 1
                while (n+length) in nums:
                    length += 1
                longest = max(length, longest)
        
        return longest