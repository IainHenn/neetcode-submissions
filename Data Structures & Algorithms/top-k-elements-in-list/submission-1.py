class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq.keys():
                freq[num] += 1
            else:
                freq[num] = 1
        
        k_list = []

        for i in range(k):
            highest = -1
            highestVal = -1
            for key, value in freq.items():
                if freq[key] >= highestVal and key not in k_list:
                    highest = key
                    highestVal = freq[key]
            k_list.append(highest)
        
        return k_list

