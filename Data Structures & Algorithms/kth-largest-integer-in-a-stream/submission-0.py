class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        temp_nums = sorted(self.nums, reverse=True)
        temp_k = self.k
        while temp_k > 1:
            print(f"{self.nums} /w k={self.k}: {temp_nums}")
            temp_nums.pop(0)
            temp_k -= 1
        
        print(f"returning: {temp_nums[0]}")
        return temp_nums[0]

