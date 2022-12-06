//Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
// The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number 
// and column number of the current cell, and i2, j2 are the row number and 
// column number of the nearest cell having value 1.
 

// Example 1:

// Input: grid = {{0,1,1,0},{1,1,0,0},{0,0,1,1}}
// Output: {{1,0,0,1},{0,0,1,1},{1,1,0,0}}
// Explanation: The grid is-
// 0 1 1 0 
// 1 1 0 0 
// 0 0 1 1 
// 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and
// (2,1) are at a distance of 1 from 1's at (0,1),
// (0,2), (0,2), (2,3), (1,0) and (1,1)
// respectively.


#include <bits/stdc++.h>
using namespace std;

vector<vector<int>>nearest(vector<vector<int>>grid)
	{

     int n = grid.size(), m = grid[0].size();

     vector<vector<int>>ans(n,vector<int>(m,0));

     vector<vector<bool>>visited(n,vector<bool>(m,false));

     queue<pair<pair<int,int>,int>>q;

     

     for(int i=0;i<n;i++){

         for(int j=0;j<m;j++){

             if(grid[i][j]){

                 q.push({{i,j},0});

                 visited[i][j] = true;

             }

         }

     }

     

     int dx[4] = {-1,1,0,0};

     int dy[4] = {0,0,-1,1};

     

     while(!q.empty()){

         auto p = q.front();

         q.pop();

         int x = p.first.first, y = p.first.second, dist = p.second;

         ans[x][y] = dist;

         

         for(int i=0;i<4;i++){

             int nx = x + dx[i];

             int ny = y + dy[i];

             if(nx >= 0 && ny >= 0 && nx <= n-1 && ny <= m-1 && !visited[nx][ny]){

                 visited[nx][ny] = true;

                 q.push({{nx,ny},dist+1});

             }

         }

     }

     

     return ans;
	    // Code here
	}