class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Split into two
        # 1. get the first tallest line
        # 2. find the max container of water 
        # I think that I can do this all in one loop where each iteration checks the 
        
        l, r = 0, len(heights) - 1
        ans = 0
        while l < r:
            ans = max(ans, (r - l) * min(heights[r], heights[l]))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans