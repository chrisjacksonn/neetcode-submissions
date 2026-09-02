class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        # creating a hashmap with the character count as the 
        # key, and list of anagrams as the value
        for s in strs:
            count = [0] * 26 # each possible character

            for c in s:
                # adding an index to each letter
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())



