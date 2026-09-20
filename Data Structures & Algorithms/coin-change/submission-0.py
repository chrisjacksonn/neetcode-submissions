class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # table: dp[a] = fewest coins to pay exactly a cents (index = cents, value = coin count)
        # every slot starts as amount + 1, a fake "impossible" value no real answer can reach
        dp = [amount + 1] * (amount + 1)
        # paying 0 cents takes 0 coins
        dp[0] = 0

        # solve every total from 1 cent up, so smaller totals are ready to look up
        for a in range(1, amount + 1):
            # don't pick a coin, try putting down each one
            for c in coins:
                # skip coins bigger than the total
                if a - c >= 0:
                    # a - c = cents still owed, dp[a - c] = coins that takes, + 1 for the coin put down
                    # keep whichever coin gives the smallest total
                    dp[a] = min(dp[a], 1 + dp[a - c])
        # still the fake value means the total can't be made, so -1
        return dp[amount] if dp[amount] != amount + 1 else -1