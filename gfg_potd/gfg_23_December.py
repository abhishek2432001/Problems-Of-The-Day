'''Burst Balloons
HardAccuracy: 60.57%Submissions: 289+Points: 8
Lamp
You can earn more Geekbits by participating in GFG Weekly Coding Contest  

You are given N balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array arr. You are asked to brust all the balloons.
If you brust the ith  balloon,, you will get arr[ i - 1 ] * arr[ i ] * arr[ i + 1] coins. If i - 1, or i + 1 goes out of bounds of the array, consider it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by brusting the balloons wisely.

Example 1:

Input:
N = 4
arr[ ] = {3, 1, 5, 8}
Output: 167
Explanation: 
arr[ ] = {3, 1, 5, 8}  - - > {3, 5, 8} - - > {3, 8} - - > { 8} - -> { }
coins = 3 *1 *5,      +      3*5*8     +   1*3*8   +  1*8*1   = 167'''

def maxCoins(N, arr):
        dp = [[-1] * i for i in range(1, N + 1)]
        for diff in range(N):
            for lo in range(N - diff):
                hi = lo + diff
                sides = 1
                if lo > 0:
                    sides *= arr[lo - 1]
                if hi < len(dp) - 1:
                    sides *= arr[hi + 1]
                for i in range(lo, hi + 1):
                    score = arr[i] * sides
                    if i > lo:
                        score += dp[i - 1][lo]
                    if hi > i:
                        score += dp[hi][i + 1]
                    dp[hi][lo] = max(dp[hi][lo], score)
        return dp[N - 1][0]