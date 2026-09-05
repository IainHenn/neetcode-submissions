class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = []
        for i in range(0,len(nums)):

            product = None
            for j in range(0,len(nums)):
                if i != j:
                    if product is None:
                        product = nums[j]
                    else:
                        product = product * nums[j]
            products.append(product)

        return products

            
            
