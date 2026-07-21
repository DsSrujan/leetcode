class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}

        # Count each character in magazine
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Check if ransomNote can be formed
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True