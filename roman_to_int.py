# convert roman number into an integer
# cases for subtraction: I is before V or X, then -1, X is before L or C then -10, C is before D or M -100

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {
            "I":1, 
            "V":5, 
            "X":10, 
            "L":50, 
            "C":100, 
            "D":500, 
            "M":1000
            }

        sum = 0

        for i in range(len(s)):
            # cases for subtraction
            if i < len(s) -1:
                if (s[i] == "I" and s[i + 1] == "V") or (s[i] == "I" and s[i + 1] == "X"):
                    sum -= 1
                elif (s[i] == "X" and s[i + 1] == "L") or (s[i] == "X" and s[i + 1] == "C"):
                    sum -= 10
                elif (s[i] == "C" and s[i + 1] == "D") or (s[i] == "C" and s[i + 1] == "M"):
                    sum -= 100
                # otherwise just add the number associated in the dict
                else:
                    sum += roman_dict[s[i]]
            else:
                sum += roman_dict[s[i]]

        return sum
