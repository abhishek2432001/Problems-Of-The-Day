'''Given an integer N. Find maximum LCM (Least Common Multiple) that can be obtained from four numbers less than or equal to N.
Note: Duplicate numbers can be used.

Example 1:

Input:
N = 4
Output: 12
Explanation:
The four numbers can be [4,4,3,2] or
[4,4,4,3], etc. It can be shown that 12 is
the maximum LCM of four numbers that can
be obtained from numbers less than or equal 
to 4.'''

class Solution:    
    def maxGcd(self,N):
        ans1=N*(N-1)
        ans2=(N-1)*(N-2)
        i1=N-2
        

        count=0
        while i1>=0:
            if math.gcd(ans1, i1)==1:
                ans1*=i1
                count+=1
            if count==2:
                break
            i1-=1
        i2=N-3
        count=0
        while i2>=0:
            if math.gcd(ans2, i2)==1:
                ans2*=i2
                count+=1
            if count==2:
                break
            i2-=1
        return max(ans1, ans2)

