class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s=set()
        for n in sentence:
            if n not in s:
                s.add(n)
        return len(s)==26
