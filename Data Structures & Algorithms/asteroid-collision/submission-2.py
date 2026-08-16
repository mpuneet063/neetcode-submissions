class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while stk and a < 0 and stk[-1] > 0:
                k = a + stk[-1]
                if k < 0:
                    stk.pop()
                elif k > 0:
                    a = 0
                else:
                    a = 0
                    stk.pop()
            if a:        stk.append(a) 
        return stk
    