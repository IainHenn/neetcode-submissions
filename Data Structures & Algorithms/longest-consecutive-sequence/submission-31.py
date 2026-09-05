class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))

        longest = 0

        for i in range(len(nums)):
            # If it doesn't have a left number, it's the start of a sequence
            if nums[i] - 1 not in nums:
                length = 0
                while (nums[i] + length) in nums:
                    length += 1
                longest = max(longest, length)

            
        return longest