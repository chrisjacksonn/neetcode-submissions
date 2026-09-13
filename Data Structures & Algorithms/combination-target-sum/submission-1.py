class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, cur, total):
            # final value is found to reach target
            if total == target:
                # append the final value into the arr
                res.append(cur.copy())
                return
            
            # if we're past all possible scenarios or total > target
            if i >= len(nums) or total > target:
                return
            
            # final value hasn't been found, more to check...
            cur.append(nums[i]) # add curr to the combination
            dfs(i, cur, total + nums[i]) # use this number again branch
            cur.pop() # undo the choice
            dfs(i+1, cur, total) # use the next number branch

        dfs(0, [], 0) # kick off the search starting at index 0, empty combination, total of 0
        return res        