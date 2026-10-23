class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        area=0
        stack=[]
        for i, h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                area=max(area,height*(i-index))
                start=index
            stack.append((start,h))

        for i,h in stack:
            area=max(area,(len(heights)-i)*h)
            
        return area