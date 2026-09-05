class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_hash = {}
        t_hash = {}

        for let in s:
            if let in s_hash.keys():
                s_hash[let] = s_hash[let] + 1
            else:
                s_hash[let] = 1 

        for let in t:
            if let in t_hash.keys():
                t_hash[let] = t_hash[let] + 1
            else:
                t_hash[let] = 1 

        print(f"s_hash: {s_hash}\n")
        print(f"t_hash: {t_hash}\n")

        for let in s_hash:
            if let not in t_hash:
                return False
            elif t_hash[let] != s_hash[let]:
                return False

        if len(s_hash.keys()) != len(t_hash.keys()):
            return False
        
        return True