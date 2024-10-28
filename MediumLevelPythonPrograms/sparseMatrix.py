"""
A sparse matrix is a matrix in which most of the elements are zero.
It is the opposite of a dense matrix, where most of the elements are non-zero.

Sparse matrices are often encountered in applications where a significant amount of data is absent or irrelevant,
such as in scientific computing, graph theory, machine learning (especially in high-dimensional datasets),
and large-scale linear algebra problems.

Example of a Sparse Matrix:
Consider the following 4x4 matrix:

1  0  0  0
0  0  2  0
0  0  0  0
3  0  0  4

This matrix has only 4 non-zero elements (1, 2, 3, and 4) out of 16 elements, making it sparse.

In COO format, this matrix can be represented as:

Row Indices:    [0, 1, 3, 3] row index of a non-zero value
Column Indices: [0, 2, 0, 3] column index of a non-zero value
Values:         [1, 2, 3, 4]  all the non-zero values

"""
sparseMatrix=[[0,0,0,3,4],
              [0,1,2,0,0],
              [9,8,0,0,0],
              [0,0,0,0,0]];

size=0;   #size - total number of non-zero elements

for i in range(4):
    for j in range(5):
        if(sparseMatrix[i][j]!=0):
            size+=1;

# Alternate solution to calculate size  (Using list comprehension)

"""
nonzerosInSparse=[element for row in sparseMatrix for element in row if(element!=0)];

size=len(sparseMatrix);

"""

col=size;
row=3;

compactMatrix=[[0 for i in range(col)]for j in range(row)];  # Creating an empty 2D array

k=0;

for i in range(4):
    for j in range(5):
        if(sparseMatrix[i][j]!=0):
            compactMatrix[0][k]=i;
            compactMatrix[1][k]=j;
            compactMatrix[2][k]=sparseMatrix[i][j];
            k+=1;

print("Printing compact matrix :");

for x in compactMatrix:
    print(x);
