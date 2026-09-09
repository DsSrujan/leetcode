class Solution(object):

  def isAnagram(self, s, t):
    if len(s)!=len(t):
        return False
    d={}
    for i in s :
        d[i]=d.get(i,0)+1
    for  j in t:
        if d.get(j,0)==0:
            return False 
        d[j]-=1

    return True 
