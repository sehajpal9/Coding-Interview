# given an integer, return the integer in reverse with proper signage
# for example: x = -321, return -123


class Solution:
    def reverse(self, x: int) -> int:
        
        string_x = str(x)
        sign = ""

        # if the int is negative
        if "-" in string_x:
            sign = "-"
            string_x = string_x[1:len(string_x)]
    
        # reverse the string 
        string_x = string_x[::-1]

        #print("sign: ", sign)
        #print("string: ", string_x)

        # add the sign
        final = sign + string_x

        if int(final) <= -2**31 or int(final) >= (2**31) - 1:
            return 0
        #print("final int: ", final)
        return int(final)
