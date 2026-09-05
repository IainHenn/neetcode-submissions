class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums, target, start):
            if len(nums) == 1 and nums[0] != target:
                return -1
            else:
                mid_idx = len(nums) // 2
                if nums[mid_idx] == target:
                    return mid_idx + start
                elif nums[mid_idx] < target:
                    return binary_search(nums[mid_idx:], target, start + mid_idx)
                elif nums[mid_idx] > target:
                    return binary_search(nums[:mid_idx], target, start)
            
        return binary_search(nums, target, 0)
