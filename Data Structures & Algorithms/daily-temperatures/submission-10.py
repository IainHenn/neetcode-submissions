class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        li = []
        for i in range(len(temperatures)):

            stack = temperatures[i+1:]
            curr_temp = temperatures[i]

            print(f"stack for {temperatures[i]}: {stack}")

            i = 1
            done = False
            while len(stack) != 0:
                curr = stack.pop(0)
                if curr > curr_temp:
                    li.append(i)
                    done = True
                    break
                else:
                    i += 1
            
            if len(stack) == 0 and done is not True:
                li.append(0)

        return li
