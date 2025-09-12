# return the length of the longest substring without repeating characters
# for example: s = abcabcbb, return 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0 or len(s) >= 5e4:
            return 0
        
        max_count = 1

        for i in range(len(s)):
            seen = s[i]
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen += s[j]
                    # can also do this 
                    # seen = s[i:j+1]
                    max_count = max(max_count, len(seen))
                #print(seen)
        
        return max_count
