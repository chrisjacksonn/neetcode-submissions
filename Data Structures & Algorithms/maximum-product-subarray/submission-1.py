class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # start with first element, not 0, so an all-negative array like [-5] works
        res = nums[0]
        # neutral starting values so the first multiplication is a no-op
        curMin, curMax = 1, 1

        for num in nums:
            # save old curMax * num, since curMax is overwritten before curMin needs it
            tmp = curMax * num
            # biggest product ending here: extend the max, extend the min
            # (negative * negative flips to big positive), or start fresh at num
            curMax = max(num * curMax, num * curMin, num)
            # smallest product ending here: same three options, kept around
            # in case a later negative flips it into the new max
            curMin = min(tmp, num * curMin, num)
            # best subarray could end anywhere, so check at every element
            res = max(res, curMax)
        # largest product of any contiguous subarray
        return res