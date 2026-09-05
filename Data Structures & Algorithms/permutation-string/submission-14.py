class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)):
            print(s2[i:i+len(s1)])
            
            current_window = s2[i:i+len(s1)]
            is_permutation = True
            print(f"comparing {s1} to {current_window}")

            s1_count = {}
            for letter in s1:
                if letter not in s1_count.keys():
                    s1_count[letter] = 1
                else:
                    s1_count[letter] += 1
            
            for letter in current_window:
                if letter in s1_count.keys():
                    s1_count[letter] -= 1
            
            for key, val in s1_count.items():
                if val != 0:
                    is_permutation = False
            
            if is_permutation is True:
                return True

        return False