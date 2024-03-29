from UpperTriangularDet import determinantOfUpperTriangularMatrix
from cramersRule import cramersRule
import random
import copy
import matplotlib.pyplot as plt
import time


def matrixGenerator(n):
    #Generates Random Int Values to be Stored in the nxn matrix
    mat1 = [[random.randint(1,5) for j in range(n)] for i in range(n)]
    mat2 = copy.deepcopy(mat1)
    return mat1, mat2


x = [i for i in range (1,11)]
y = []
y1 = []

#Times each run for each nxn matrix

for i in range (1,11):
    mat1, mat2 = matrixGenerator(i)
    start = time.time()
    print("Determinant of an "+ str(i)+"x"+ str(i)+ " matrix using Upper Triangular Method : ", determinantOfUpperTriangularMatrix(mat1, i))
    end = time.time()
    y.append(end-start)

    start2 = time.time()
    print("Determinant of an "+ str(i)+"x"+ str(i)+ " matrix using Cramer's Rule : ", cramersRule(mat2))
    end2 = time.time()
    y1.append(end2-start2)

# Plotting the results
plt.plot(x, y, label = "Upper Triangular")
plt.title("Runtime using Upper Triangular Method to find the Determinant of an nxn Matrix as f(n)")
plt.xlabel('Dimensions (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
plt.cla()
plt.plot(x, y1, label = "Cramer's Rule", color = "orange")
plt.title("Runtime using Cramer's Rule to find the Determinant of an nxn Matrix as f(n)")
plt.xlabel('Dimensions (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
plt.cla()
plt.plot(x, y, label = "Upper Triangular")
plt.plot(x, y1, label = "Cramer's Rule")
plt.title('Comparing Runtimes of Finding the Determinant of an nxn Matrix as f(n)')
plt.xlabel('Dimensions (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()

