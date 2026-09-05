class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []
        for i in range(0,len(height)):
            temp_left = height[:i]
            max_left_num = -999
            for number in temp_left:
                if number > max_left_num:
                    max_left_num = number
            max_left.append(max_left_num)

            temp_right = height[i:]
            max_right_num = -999
            for number in temp_right:
                if number > max_right_num:
                    max_right_num = number
            max_right.append(max_right_num)
        
        water = 0
        for i in range(0, len(height)):
            num = min(max_left[i], max_right[i]) - height[i]
            if num > 0:
                water += num
            
        return water

            