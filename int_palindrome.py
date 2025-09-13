# return true if the int is a palindrome or false if it is not 
# for example: input: 121 output: true ... input: -121 output: false

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def reverse(s):
            return s == s[::-1]

        if x <= -2**31 or x >= 2**31 - 1:
            return False

        str_x = str(x)

        if reverse(str_x):
            return True
        else:
            return False
