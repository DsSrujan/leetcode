class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for w in strs:
            a="".join(sorted(w))
            if a not in d:
                d[a]=[w]
            else:
                d[a].append(w)
        return list(d.values())
