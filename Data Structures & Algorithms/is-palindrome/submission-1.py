class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [string if string.isalnum() == True else "" for string in s]
        s_final = ""

        for string in s:
            if string != "":
                s_final += string

        i = 0
        j = len(s_final) - 1
        while i < j:
            if s_final[i].lower() != s_final[j].lower():
                return False
            i += 1
            j -= 1
        return True