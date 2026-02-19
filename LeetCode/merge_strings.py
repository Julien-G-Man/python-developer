"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for l1, l2 in zip(word1, word2):
            merged.append(l1)
            merged.append(l2)
            
        if len(word1) < len(word2):
            for i in range(len(word1), len(word2)):
                merged.append(word2[i])
        else:
            for i in range(len(word2), len(word1)):
                merged.append(word1[i])        
                     
        print(merged)
        merged_string = ''.join(merged) 
        print(merged_string)   
        
        return merged_string

# instantiation
solution = Solution()
solution.mergeAlternately("boyfriend", "girl")