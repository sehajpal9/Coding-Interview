# given a string return if it is a valid palindrome. ignore all characters that are not letters or numbers 
# for example: input = "A man, a plan, a canal: Panama" output = true ... input = "0P" output = false
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def reverse(s):
            return s == s[::-1]

        only_chars = ""

        for char in s:
            if char.isalpha() or char.isdigit(): 
                only_chars += char
        
        if reverse(only_chars.lower()):
            return True
        else:
            return False
