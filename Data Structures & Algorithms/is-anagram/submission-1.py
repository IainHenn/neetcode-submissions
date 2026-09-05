class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        
        if len(s) != len(t):
            return False
            
        for let in s:
            if let not in sMap.keys():
                sMap[let] = 1
            else:
                sMap[let] += 1

        for let in t:
            if let not in tMap.keys():
                tMap[let] = 1
            else:
                tMap[let] += 1
        
        for key, _ in sMap.items():
            if key not in tMap.keys():
                return False
            if sMap[key] != tMap[key]:
                return False
        
        return True
            