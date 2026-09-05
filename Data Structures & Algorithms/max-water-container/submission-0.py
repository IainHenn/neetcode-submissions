class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1

        max_area = -1

        while end > start:
            
            if (end - start) * min(heights[end], heights[start]) > max_area:
                max_area = (end - start) *  min(heights[end], heights[start])
            
            if heights[end] > heights[start]:
                start += 1
            
            elif heights[start] > heights[end]:
                end -= 1

            elif heights[start] == heights[end]:
                start += 1
                end -= 1

        return max_area