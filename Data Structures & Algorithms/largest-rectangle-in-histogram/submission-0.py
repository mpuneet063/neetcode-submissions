class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        area = 0
        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                index, height = stk.pop()
                area = max(area, height*(i-index))
                start = index
            stk.append((start, h))
        for i , h in stk:
            area = max(area, h*(len(heights)-i))
        return area