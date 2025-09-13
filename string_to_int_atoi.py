# convert a string to an int
# rules: spaces should be ignored until a character occurrs, if the character is a digit it is valid, it is a sign add it to sign, and if its something else ignore it
# for example: intput: "      -042", output: -24 ... input: "0-1" output: 0 ... input: "      +  123" output: 0 (because following sign was a space) ... input: 1232c82 output: 1232

class Solution:
    def myAtoi(self, s: str) -> int:
        
        acceptable = ["+", "-", " "]
        if s == "" or (s[0].isdigit() == False and s[0] not in acceptable):
            return 0

        final_s = ""
        sign = ""

        for i in range(len(s)):
            print("sign: ", sign, " final_s: ", final_s)
            if s[i] == " " and len(final_s) == 0 and sign == "":
                continue
            elif (s[i] == "+" or s[i] == "-") and len(final_s) <= 0:
                if sign != "":
                    return 0
                else: 
                    sign = s[i]
            elif s[i] == "+" or s[i] == "-" and len(final_s) > 0:
                break
            elif s[i].isdigit():
                final_s += s[i]
            else:
                break

        if final_s == "":
            return 0
        
        final = sign + final_s

        if int(final) <= -2**(31):
            return -2**(31)
        elif int(final) >= 2**(31) -1:
            return 2**(31) -1
        else:
            return int(final)
