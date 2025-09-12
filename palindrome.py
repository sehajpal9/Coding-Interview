# return the longest substring palindrome
# for example: s = bababb, return bab

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def reverse(string):
            # return true/false if string is the same in reverse
            return string == string[::-1]

        if len(s) <= 1:
            return s
        
        pal = []
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                #print(len(s[i:j]))
                if reverse(s[i:j]) == True and len(s[i:j]) > len(pal):
                    pal = s[i:j]
                    #print(pal)
        
        return pal
