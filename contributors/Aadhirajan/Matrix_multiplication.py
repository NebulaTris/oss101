import numpy
a=[[0,0,0],[0,0,0],[0,0,0]]
b=[[0,0,0],[0,0,0],[0,0,0]]
c=[[0,0,0],[0,0,0],[0,0,0]]
print("Enter the value of matrix A:")
for d in range(len(a)):
    for e in range(len(a)):
        a[d][e]=int(input(f"a[{d}][{e}]: "))
print("Enter the value of matrix B:")
for d in range(len(a)):
    for e in range(len(a)):
        b[d][e]=int(input(f"b[{d}][{e}]: "))
#using first principle for matrix multiplication
i=0
j=0
k=0
for i in range(len(a)):
    for j in range(len(a)):
        sum=0
        for k in range(len(a)):
            sum=sum+a[i][k]*b[k][j]
        c[i][j]=sum
print(c)
#using numpy library
x=numpy.mat(a)
y=numpy.mat(b)
print(x*y)