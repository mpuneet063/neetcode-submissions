class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        # If the largest element exceeds target, we can't partition
        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(index: int) -> bool:
            if index == len(nums):
                return True

            for j in range(k):
                if buckets[j] + nums[index] <= target:
                    buckets[j] += nums[index]

                    if backtrack(index + 1):
                        return True

                    buckets[j] -= nums[index]

                # Pruning: If bucket is empty, trying subsequent empty buckets is redundant
                if buckets[j] == 0:
                    break

            return False

        return backtrack(0)