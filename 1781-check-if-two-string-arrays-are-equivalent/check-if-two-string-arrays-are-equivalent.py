class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = "".join(word1)
        b = "".join(word2)
        return True if a == b else False