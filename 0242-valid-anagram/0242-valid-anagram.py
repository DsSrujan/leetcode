class Solution(object):

  def isAnagram(self, s, t):
    dic1={}
    dic2={}
    if len(s)!=len(t):
        return False
    for n,m in zip(s,t):
        dic1[n]= dic1.get(n,0)+1
        dic2[m]= dic2.get(m,0)+1
    return dic1==dic2
