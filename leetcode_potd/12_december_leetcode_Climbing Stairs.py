'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps'''

def climbStairs(n):
    if n == 1:
        return 1

    dp = {}
    dp[1] = 1
    dp[2] = 2
    
    i=3
    while i <= n :
        dp[i] = dp[i - 1] + dp[i - 2]
        i+=1
    return dp[n]