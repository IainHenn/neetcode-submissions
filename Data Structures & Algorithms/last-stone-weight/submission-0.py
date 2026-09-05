class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            temp_sorted = sorted(stones, reverse=True)
            
            x = temp_sorted[0]
            y = temp_sorted[1]

            print(f"stones before: {stones}")
            print(f"x: {x}\ny:{y}")

            if x == y:
                stones.remove(x)
                stones.remove(y)

                print(f"stones after: {stones}")

            elif x < y: 
                og_idx = stones.index(y)
                stones[og_idx] = y - x
                stones.remove(x)
            
            elif y < x:
                og_idx = stones.index(x) 
                stones[og_idx]= x - y
                stones.remove(y)

                print(f"stones after: {stones}")
            
        
        return stones[0] if len(stones) == 1 else 0

        