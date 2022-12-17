'''2D Hopscotch'''
def hopscotch(n, m, mat, ty, i, j):
    if ty==0:

        sm=0

        

        if j%2!=0:

            arr=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1]]

            for k in arr:

                i1=i+k[0]

                j1=j+k[1]

                if i1>=0 and j1>=0 and i1<n and j1<m:

                    sm+=mat[i1][j1]
        else:

            arr=[[-1,-1],[-1,1],[1,0],[0,1],[-1,0],[0,-1]]

            for k in arr:

                i1=i+k[0]

                j1=j+k[1]

                if i1>=0 and j1>=0 and i1<n and j1<m:

                    sm+=mat[i1][j1]

    else:

        sm=0

        if j%2==1:

            arr=[[-1,1],[-1,-1],[2,0],[-2,0],[2,-1],[2,1],[-1,-2],[-1,2],[0,-2],[0,2],[1,-2],[1,2]]

            for k in arr:

                i1=i+k[0]

                j1=j+k[1]

                if i1>=0 and j1>=0 and i1<n and j1<m:

                    sm+=mat[i1][j1]

                    # print(i1,j1)

                    # print(sm)

        else:

            arr=[[-2,1],[1,-1],[2,0],[-2,0],[-2,-1],[1,1],[-1,-2],[-1,2],[0,-2],[0,2],[1,-2],[1,2]]

            for k in arr:

                i1=i+k[0]

                j1=j+k[1]

                if i1>=0 and j1>=0 and i1<n and j1<m:

                    sm+=mat[i1][j1]

    return sm