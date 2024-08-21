class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        minlen = min(len(word1),len(word2))
        for i in range(minlen):
            merged += word1[i] + word2[i]
        if len(word1) < len(word2):
            merged += word2[i+1:]
        else:
            merged += word1[i+1:]
        return merged
        