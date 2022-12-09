# '''Given the chessboard dimensions. Find out the number of ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.

# Note:
# The knights have to be placed on different squares. A knight can move two squares horizontally and one square vertically (L shaped), or two squares vertically and one square horizontally (L shaped). The knights attack each other if one can reach the other in one move.

# Example 1:

# Input:
# N = 2, M = 2
# Output: 12 
# Explanation: There are 12 ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.
# '''

#include <bits/stdc++.h>
using namespace std;


long long numOfWays(int N, int M)
{
    // write code here
    long long mod=1e9+7;

    long long sub=0;

    if (M>2 and N>1) sub=(((4*(M-2))%mod)*(N-1))%mod;

    if (N>2 and M>1) sub=(sub+(((4*(N-2))%mod)*(M-1))%mod)%mod;

    long long ans = (long long)(((N*M)%mod)*((N*M-1)%mod) - sub + mod)%mod; 

    return ans;
}