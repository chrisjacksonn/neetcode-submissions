class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            else: 
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1
            
        return -1
    


            



        # need o(log n)
        # utilize binary tree search
        # find the target based on binary tree search 
        # return index of the value
        # if binary tree search cannot nail down the value, return -1
        