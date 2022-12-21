// 886. Possible Bipartition
// We want to split a group of n people (labeled from 1 to n) into two groups of any size. 
// Each person may dislike some other people, and they should not go into the same group.
// Given the integer n and the array dislikes where dislikes[i] = [ai, bi] 
// indicates that the person labeled ai does not like the person labeled bi, return true 
// if it is possible to split everyone into two groups in this way.
// Example 1:
// Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
// Output: true
// Explanation: group1 [1,4] and group2 [2,3].
// Example 2:
// Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
// Output: false
// Example 3:
// Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
// Output: false
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        
    std::vector<std::vector<int>> adjacencyList(n + 1);
    std::vector<int> colorOfIndex(n + 1, -1);

    for (int i = 0; i < dislikes.size(); i++)
    {
        adjacencyList[dislikes[i][0]].emplace_back(dislikes[i][1]);
        adjacencyList[dislikes[i][1]].emplace_back(dislikes[i][0]);
    }

    std::queue<int> personQueue;

    //Iterate through all of the people. If they're marked as unvisited,
    //explore that person and the rest of their adjacency list (dislikes)
    for (int i = 1; i <= n; i++)
    {
        if (colorOfIndex[i] == -1)
        {
            colorOfIndex[i] = 1;
            personQueue.emplace(i);
        }

        while (personQueue.empty() == false)
        {
            int person = personQueue.front();
            personQueue.pop();

            for (int hatedPerson : adjacencyList[person])
            {
                if (colorOfIndex[hatedPerson] == -1)
                {
                    colorOfIndex[hatedPerson] = 1 - colorOfIndex[person];
                    personQueue.emplace(hatedPerson);
                }
                else if (colorOfIndex[hatedPerson] == colorOfIndex[person])
                {
                    return false;
                }
            }
        }
    }

    return true;
    }
};