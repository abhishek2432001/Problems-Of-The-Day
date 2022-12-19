// Alex Travelling
// Alex is very fond of traveling. There are n cities, labeled from 1 to n.  
// You are also given flights, a list of travel flights as directed weighted edges
//  flights[i] = (ui,vi,wi) where ui is the source node, vi is the target node,
//   and wi is the price it takes for a person to travel from source to target.
// Currently, Alex is in k'th city and wants to visit one city of his choice. 
// Return the minimum money Alex should have so that he can visit any city of his choice from k'th city.
//  If there is a city that has no path from k'th city, which means Alex can't visit that city, return -1. 
// Alex always takes the optimal path. He can any city via another city by taking multiple flights.
// Example 1:
// Input:
// n: 4
// k: 2
// flights size: 3
// flights: [[2,1,1],[2,3,1],[3,4,1]]
// Output:
// 2
// Explanation:
// to visit 1 from 2 takes cost 1
// to visit 2 from 2 takes cost 0
// to visit 3 from 2 takes cost 1
// to visit 4 from 2 takes cost 2,
// 2->3->4
// So if Alex wants to visit city 4
// from 2, he needs 2 units of money
// Example 2:
// Input:
// n: 4 
// k: 3 
// flights size: 3 
// flights: [[2,1,1],[2,3,1],[3,4,1]] 
// Output: -1
// Explanation:
// There is no direct or indirect path 
// to visit city 2 and 1 from city 3
#include <bits/stdc++.h>
using namespace std;

int minimumCost(vector<vector<int>>& f, int N, int k) {
    // code here
     vector<vector<pair<int,int>>>adj(N+1);
   vector<int>dist(N+1,INT_MAX);
   for(int i = 0 ; i <f.size();i++){
       adj[f[i][0]].push_back({f[i][1],f[i][2]});
   }
   priority_queue<pair<int,int> , vector<pair<int,int>> , greater<pair<int,int>>>q;
   dist[k] = 0;
   q.push({dist[k], k});
   while(!q.empty()){
       auto it = q.top();
       q.pop();
       int node = it.second;
       int distance = it.first;
       for(auto child : adj[node])
       {
           if(dist[child.first] > (distance + child.second)){
               dist[child.first] = (distance + child.second);
               q.push({dist[child.first] , child.first});
           }
       }
   }
   int ans = -1; 
	for(int i=1 ; i<=N;i++){
	    if(dist[i]==INT_MAX)return -1;
	    else ans= max(ans,dist[i]);
	}
	return ans;
}