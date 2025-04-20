class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        i = -1
        length = len(s)
        while (length  >= i * -1) and s[i] != " ":
            i -= 1
        i += 1
        i *= -1
        return i

        
        