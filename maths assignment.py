import numpy 
D= numpy.array([
    [1,2,3,4,5,6],
    [2,4,6,8,10,12],
    [1,0,1,0,1,0],
    [0,1,1,2,1,1],
    [1,1,2,1,3,2]
])
a=numpy.linalg.matrix_rank(D)
print("Rank of the matrix is :-",a)