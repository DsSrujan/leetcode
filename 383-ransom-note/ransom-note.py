class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Convert the magazine into a list so we can remove characters as we use them
        magazine_chars = list(magazine)
        
        for char in ransomNote:
            if char in magazine_chars:
                # Remove the used character so it can't be reused
                magazine_chars.remove(char)
            else:
                # If the character isn't available, we can't build the note
                return False
                
        return True