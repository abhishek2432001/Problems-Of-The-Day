'''Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) <= 1:
            return [0]
        stack = [len(temperatures)-1]
        ans = [0]
        for pos in range(len(temperatures)-2, -1, -1):
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[pos]:
                stack.pop()
            if len(stack) == 0:
                ans.append(0)
            else:
                ans.append(stack[-1]-pos)
            stack.append(pos)
        ans.reverse()
        return ans