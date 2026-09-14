class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        len1, len2 = len(word1), len(word2)
        
        # Use xrange for Python 2 memory optimization
        for i in xrange(min(len1, len2)):
            res.append(word1[i])
            res.append(word2[i])
            
        # Append the remaining parts of the longer string
        res.append(word1[i+1:])
        res.append(word2[i+1:])
        
        return "".join(res)
