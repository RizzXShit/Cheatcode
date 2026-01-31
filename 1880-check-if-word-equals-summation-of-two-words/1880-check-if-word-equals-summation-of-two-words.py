class Solution(object):
    def isSumEqual(self,firstWord, secondWord, targetWord):
        def convert(word):
            return int("".join(str(ord(c) - ord('a')) for c in word))
        return convert(firstWord) + convert(secondWord) == convert(targetWord)
