"""
Give an array of strings strs, group the anagrams together.
You can return the answer in any order.

Example 1:
input: strs = ["eat", "tea", "ate", "nat", "bat"]
output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Explanation

Anagrams have the same letters with the same frequency, only in a different order.
The usual way to group them is to build a hash map where each key represents the
letter-count pattern of a word.

One simple key is the sorted version of the string:
- "eat" -> "aet"
- "tea" -> "aet"
- "nat" -> "ant"

Words with the same key are collected into the same list.
"""

def groupAnagrams(strs):
    """Group anagrams using sorted string as key."""
    groups = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

strs = ["eat", "tea", "ate", "nat", "bat", "fear", "raef", "real", "man", "amn"]
print(groupAnagrams(strs))