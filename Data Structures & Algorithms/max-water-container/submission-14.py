class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        l, r = 0, len(heights) - 1

   

        while l < r:
            h = min(heights[l], heights[r])
            w = (r - l)
            area = h * w
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r] or heights[l] == heights[r]:
                r -= 1
        return res




        # l, r 
            # compare, larger height stays, shift the other pointer
                # before shifting, record the area for the indices
            # continue in a loop until indices meet
            # once they meet, return largest area recorded