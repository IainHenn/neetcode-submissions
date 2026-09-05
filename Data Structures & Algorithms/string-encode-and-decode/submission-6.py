class Solution:

    def encode(self, strs: List[str]) -> str:
        strToReturn = ""
        for string in strs:
            strToReturn += (f"{len(string)},_" + string)
        
        return strToReturn

    def decode(self, s: str) -> List[str]:
        print(s)
        sizes = []
        res = []
        i = 0
        
        while i < len(s):
            while i < len(s) and s[i] != "_":
                #While not hashtag and not greater than the length
                curr = ""
                while s[i] != ",":
                    curr += s[i]
                    i += 1
                #If while stops, then append the size, and increment i by size + "," + "#"
                sizes.append(int(curr))
                length = int(curr)
                i += 2

                res.append(s[i:i + length])
                i += length
        return res
