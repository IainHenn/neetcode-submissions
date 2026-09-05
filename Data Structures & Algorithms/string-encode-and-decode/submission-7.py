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

                #Length of word
                length = int(curr)

                #Increase past the "," and "#"
                i += 2

                #Get between i (start of word) to end of word (i + length)
                res.append(s[i:i + length])

                #Increment past the length to the next word
                i += length
        return res
