class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        seen = {}

        for i in range(len(s)):
            if s[i] not in seen.keys():
                seen[s[i]] = 1
            elif s[i] in seen.keys():
                seen[s[i]] = seen[s[i]] + 1

        print(f"after s: {seen}")

        for i in range(len(t)):

            if t[i] not in seen.keys():
                return False
            
            else:
                seen[t[i]] -= 1
        
        print(seen)
        
        for i, j in seen.items():
            if j != 0:
                return False

        return True
        
