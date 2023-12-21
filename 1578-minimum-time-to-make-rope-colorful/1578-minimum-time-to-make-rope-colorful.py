class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        ans = 0
        i = 1
        while i < len(colors):
            
            max_ = neededTime[i-1]
            sum_ = neededTime[i-1]
            j = i
            while j < len(colors) and colors[j] == colors[j-1]:
                max_ = max(max_, neededTime[j])
                sum_ += neededTime[j]
                j += 1
                i = j - 1
            i += 1
        
            ans += (sum_ - max_)

        return ans