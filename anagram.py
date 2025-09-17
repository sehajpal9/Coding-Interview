# given a string s and another string t, return True if t is an anagram or False otherwise 
# for example: s = "aacc" t = "cacc" return False ... s = "anagram" t = "nagaram" return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False

        for letter in t:
            if letter in s:
                s = s.replace(letter, "", 1)
            else:
                return False

        return True
