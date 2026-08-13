class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            diff = limit - people[r]
            # people.pop()
            r -= 1
            boats += 1
            if l <= r and people[l] <= diff:
                l += 1
        
        return boats