class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # output will be len of input arr
        res = [1] * (len(nums))

        prefix = 1

        # Need the value only → for i in nums
        # however, Need the position → for i in range(len(nums))
        for i in range(len(nums)):
            # placing each prefix in that index's spot for now
            res[i] = prefix
            # update prefix
            # multiply it by the index you're at
            prefix *= nums[i]
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

