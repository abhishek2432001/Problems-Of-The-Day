#include <bits/stdc++.h>
using namespace std;

int miniavgdiff(vector<int>nums){
	int n=nums.size();
        long long prefix[n],suffix[n];
        prefix[0]=nums[0];
        suffix[n-1]=nums[n-1];
        
        for(int i=1;i<n;i++)
        {
            prefix[i]=nums[i]+prefix[i-1];
        }
        
        for(int i=n-2;i>=0;i--)
        {
            suffix[i]=nums[i]+suffix[i+1];
        }
        long long mn=INT_MAX,index;
        for(int i=0;i<n;i++)
        {
            long long first=prefix[i];
            first=first/(i+1);
            long long second;
            if(i==n-1) second=0;
            else
            {
                second=suffix[i+1];
                second/=(n-i-1);
            }
            if(abs(first-second)<mn)
            {
                mn=abs(first-second);
                index=i;
            }

        }
        return index;

}