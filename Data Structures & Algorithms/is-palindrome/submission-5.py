class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric chars
        s_clean = ""
        for c in s:
            if c.isalnum() is True:
                s_clean = s_clean + c

        right = len(s_clean) - 1
        left = 0  

        print(f"s_clean: {s_clean}")

        while right > left:
            
            if s_clean[right].lower() != s_clean[left].lower():
                return False

            right = right - 1
            left = left + 1 

        return True