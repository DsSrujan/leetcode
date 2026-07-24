from itertools import izip

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in izip(s, t):
            # Check s -> t mapping consistency
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False

            # Check t -> s mapping consistency
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False

            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True