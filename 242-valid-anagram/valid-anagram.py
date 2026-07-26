class Solution(object):

  def isAnagram(self, s, t):
    if len(s)!=len(t):
        return False
    fe1={}
    fe2={}
    for i in range(len(s)):
        fe1[s[i]]=fe1.get(s[i],0)+1
        fe2[t[i]]=fe2.get(t[i],0)+1
    return fe1==fe2

