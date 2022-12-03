#include <bits/stdc++.h>
using namespace std;



bool isPossible(int m,int k,vector<int> stalls)
    {
        int co_ordinate = stalls[0],cnt = 1;
        
        for(int i=1;i<stalls.size();i++)
        {
            if(stalls[i]-co_ordinate>=m)
            {
                cnt++;
                co_ordinate = stalls[i];
            }
            if(cnt==k)
            {
                return 1;
            }
        }
        return 0;
    }
int solve(int n, int k, vector<int> &stalls) {

    sort(stalls.begin(),stalls.end());
    int ans = 0;
    int l = 0,r = stalls[n-1]-stalls[0];
    while(l<=r){
        int m = l+(r-l)/2;
        if(isPossible(m,k,stalls)){
            l = m+1;
            ans = m;
        }
        else{
            r = m-1;
        }
    }
    return ans;
}

int main(){
    int n,k;
    cin>>n>>k;
    vector<int>stalls(n);
    for(int i=0;i<n;i++){
        cin>>stalls[i];
    }
    cout<<solve(n,k,stalls);
    // for input:n=5,k=3,stalls = 1,2,4,8,9
    // O/p=>3
}