class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]

        time = []
        for p,s in sorted(pair)[::-1]:
            time.append((target-p)/s)
            if len(time) >= 2 and time[-1] <= time[-2]:
                time.pop()
        n = len(time)

        return n        