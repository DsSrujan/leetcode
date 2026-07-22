class Solution(object):

  def isAnagram(self, s, t):
    if len(s) != len(t):
      return False

    counts = [0] * 26

    for i in range(len(s)):
      counts[ord(s[i]) - ord('a')] += 1
      counts[ord(t[i]) - ord('a')] -= 1

    for count in counts:
      if count != 0:
        return False

    return True