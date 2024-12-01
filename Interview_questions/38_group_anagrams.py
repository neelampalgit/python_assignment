# Group Anagrams:
#     Problem: Given a list of strings, group anagrams together.
#     Example: group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#     should return [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)
    return list(anagrams.values())

# Example usage:
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
