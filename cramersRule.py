def MinorMatrix(M, i, j): #returns a new n-1xn-1 matrix using list comprehension
    return [minor[: j] + minor[j+1:] for minor in (M[: i] + M[i+1:])]

def cramersRule(M):

    if (len(M) == 1): #if the length of a matrix is 1x1, then the determinant is equal to the single element in the matrix
        return M[0][0]
    
    if(len(M) == 2): #base case, ad - bc 
        det = M[0][0] * M[1][1] - M[1][0] * M[0][1]
        return det
    else: #recursive step, finds minor matrices and evaluates the determinant
        det = 0
        for i in range(len(M)):
            sign = (-1) ** (1+i)
            minor = MinorMatrix(M,1,i)
            # print(minor, det, sign)
            det += sign * M[1][i] * cramersRule(minor)
            
    # returns final determinant
    return(det)

