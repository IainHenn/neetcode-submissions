class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        li = []
        for i in range(len(temperatures)):
            current_largest = temperatures[i]
            current_largest_idx = 0

            for j in range(i + 1, len(temperatures)):
                if current_largest < temperatures[j]:
                    current_largest = temperatures[j]
                    current_largest_idx = j - i
                    break
            
            if current_largest == temperatures[i]:
                li.append(0)
            else:
                li.append(current_largest_idx)

        return li