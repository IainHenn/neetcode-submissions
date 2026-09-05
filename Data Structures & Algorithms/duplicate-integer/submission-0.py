class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeMap = {}
        for num in nums:
            if num in dupeMap.keys():
                return True
            else:
                dupeMap[num] = False
        return False