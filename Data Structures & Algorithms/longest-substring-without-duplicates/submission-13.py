class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 1
        charSet = set()
        maxLength = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = r - l + 1
            maxLength = max(maxLength, length)
        return maxLength



        