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
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res        