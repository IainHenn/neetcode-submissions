class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric chars
        s_clean = ""
        for c in s:
            if c.isalnum() is True:
                s_clean = s_clean + c

        left = 0
        right = len(s_clean) - 1

        while left < right:

            if s_clean[left].lower() != s_clean[right].lower():
                return False

            left += 1
            right -= 1
        
        return True