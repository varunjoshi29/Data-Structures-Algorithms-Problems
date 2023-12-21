class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = []

        i = len(temperatures) - 1

        while i >= 0:

            if len(stack) > 0:
                if stack[-1][0] > temperatures[i]:
                    ans[i] = 1
                    stack.append([temperatures[i], i])
                else:
                    while len(stack) > 0 and stack[-1][0] <= temperatures[i]:
                        stack.pop()
                    
                    if len(stack) > 0:
                        __, index = stack[-1]
                        ans[i] = index - i
                    stack.append([temperatures[i], i])
                    
            else:
                stack.append([temperatures[i], i])
            
            i -= 1
        
        return ans
