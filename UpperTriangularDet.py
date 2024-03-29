def determinantOfUpperTriangularMatrix(mat, n):
    
        temp = [0]*n  # temporary array for storing row during exchanges
        total = 1 # stores k value det(A) = det(kA) = k*det(A)
        det = 1  # initialize determinant
    
        # loop for traversing the diagonal elements
        for i in range(0, n):
            index = i  # initialize the index 
    
            # finding the index which has non zero value to skip zeros
            while(mat[index][i] == 0 and index < n):
                index += 1
    
            if(index == n):  # if there is no non zero element the determinant of matrix is zero
                continue
    
            if(index != i): # if there is a nonzero element 
                # loop for swapping the diagonal element row and index row
                for j in range(0, n):
                    mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
    
                # determinant property det(B) = -det(A)
                det = det*int(pow(-1, index-i))
    
            # storing the values of diagonal row elements
            for j in range(0, n):
                temp[j] = mat[i][j]
    
            # traversing every row below the diagonal element
            for j in range(i+1, n):
                num1 = temp[i]     # value of diagonal element
                num2 = mat[j][i]   # value of next row element
    
                # traversing every column of row and multiplying to every row
                for k in range(0, n):
                    # multiplying to make the diagonal element and next row element equal to subtract and get 0
                    mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])
    
                total = total * num1  # Det(kA)=kDet(A);
    
        # multiplying the diagonal elements to get determinant (property of upper traingular matrix)
        for i in range(0, n):
            det = det*mat[i][i]
    
        return int(det/total)  # Det(kA)/k=Det(A)
