def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''

    rowbegin = 0
    rowend = len(a)
    colbegin = 0
    colend = len(a)
    
    
    while (rowbegin < rowend and colbegin < colend):
 
        # Print the first row from
        # the remaining rows
        for i in range(colbegin, colend):
            print(a[colbegin][i], end=" ")

        rowbegin += 1
         # Print the last column from
        # the remaining columns
        for i in range(rowbegin, rowend):
            print(a[i][colend - 1], end=" ")

        colend -= 1
        #print('colend : ' + str(colend))
        # Print the last row from
        # the remaining rows
        if (rowbegin < rowend):
 
            for i in range(colend - 1, (colbegin - 1),-1):
                print(a[rowend - 1][i], end=" ")
 
            rowend -= 1

        if (colbegin < colend):
            for i in range(rowend - 1, rowbegin - 1, -1):
                print(a[i][colbegin], end=" ")
 
            colbegin += 1
          
 
         
# Driver Code
a = [[1, 2, 3,4],
     [5, 6,7,8],
     [9, 10,11, 12],
     [13,14,15,16]]
 
R = 3
C = 3
 
# Function Call
spiralPrint(R, C, a)
    
    