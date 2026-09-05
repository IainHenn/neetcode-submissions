class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        elif nums == 3 and sum(nums) == 0:
            return [nums]
        
        else:
            groups = []

            nums = sorted(nums)

            for i in range(len(nums)):
                j = i + 1
                k = len(nums) - 1


                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in groups:
                            groups.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1

                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    
            return groups
            

