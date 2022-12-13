'''Given an array arr[] of N elements and a number K. 
Split the given array into K subarrays such that the maximum subarray sum achievable out 
of K subarrays formed is minimum possible. Find that possible subarray sum.
Example 1:
Input:
N = 4, K = 3
arr[] = {1, 2, 3, 4}
Output: 4
Explanation:
Optimal Split is {1, 2}, {3}, {4}.
Maximum sum of all subarrays is 4,
which is minimum possible for 3 splits. '''

def splitArray(arr, N, k):
    def cansplit(m):
        nonlocal k, arr
        s = 0
        cnt = 1
        for e in arr:
            s += e
            if s > m:
                cnt += 1
                s = e
        return cnt <= k
    
    lo, hi = max(arr), sum(arr)+1
    while lo < hi:
        mi = lo+(hi-lo)//2
        if cansplit(mi):
            hi = mi
        else:
            lo = mi+1
    return lo