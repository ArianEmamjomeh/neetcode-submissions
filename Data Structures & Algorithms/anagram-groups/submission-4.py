from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary: key = sorted version of word, value = list of anagrams
        groups = {}

        for s in strs:
            # sorted(s) gives a *list* of characters in order, e.g. ['a', 'c', 't']
            # ''.join(...) turns that list back into a string, e.g. "act"
            key = ''.join(sorted(s))

            # if this key hasn't been seen before, create a new empty list
            if key not in groups:
                groups[key] = []

            # add the current string to the right group
            groups[key].append(s)

        # dictionary values are the lists of anagram groups
        return list(groups.values())


        