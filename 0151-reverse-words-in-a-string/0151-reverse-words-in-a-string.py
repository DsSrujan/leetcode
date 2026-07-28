class Solution(object):

    def reverseWords(self, s):
        # 1. split() strips extra whitespace and extracts all words
        # 2. [::-1] reverses the list of words
        # 3. " ".join() connects them with a single space
        return " ".join(s.split()[::-1])