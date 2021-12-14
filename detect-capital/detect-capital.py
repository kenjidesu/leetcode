class Solution(object):
    def detectCapitalUse(self, word):
        return word == word.upper() or word == word.lower() or word == word.capitalize()
        