class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group anagrams by using a sorted tuple as a shared key
        # e.g. "act" and "cat" both sort to ('a','c','t') → same group
        #
        # Walkthrough with ["act", "cat", "hat"]:
        #
        # i = "act" → key = ('a','c','t') → hashmap = { ('a','c','t'): ["act"] }
        # i = "cat" → key = ('a','c','t') → hashmap = { ('a','c','t'): ["act", "cat"] }  ← same key, so "cat" joins "act"
        # i = "hat" → key = ('a','h','t') → hashmap = { ('a','c','t'): ["act", "cat"], ('a','h','t'): ["hat"] }
        #
        # Final hashmap values → [["act", "cat"], ["hat"]]

        hashmap = {}  # { ('a','c','t'): ["act", "cat"], ... }
        result = []

        for i in strs:
            key = tuple(sorted(i))  # signature: same for all anagrams of a word
            hashmap[key] = hashmap.get(key, []) + [i]  # append word to its group, or start a new group

        for key, val in hashmap.items():
            result.append(val)  # collect each group into the result list

        return result
            


        