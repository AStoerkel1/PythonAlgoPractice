''' 
this is supposed to perform a bunch of operations for matricies
I'm too lazy to add any type checking rn
'''

import numpy as np
class matrixOps:
#A = any matrix, B = a multiplicable vector or matrix
	def __init__(self, A, B):
		self.A = A
		self.B = B

#transpose the matrix		
	def transpose(self):
		return [list(x) for x in zip(*self.A)]

#multiply matricies (i found the mat*mat alg online but modified it for vectors)
	def multMat(self):
#B is a matrix
		if type(self.B[0]) is (np.ndarray):
			return [[sum(a * b for a, b in zip(A_row, B_col))for B_col in zip(*self.B)]for A_row in self.A]
#B is a vector
		else:
			return [sum(a * b for a, b in zip(A_row, self.B)) for A_row in self.A]

#given a matrix and vector that are inconsistant, this will find the least squares solution
	def leastSquares(self):
		Atrans = self.transpose(self.A)
		ATA = self.multMat(Atrans, A)
		return np.linalg.inv(ATA).dot(self.y)

def printMat(A):
	for i in A:
		print(i)

#this is a test
A = np.array([[1, 2],[3, 4],[5,6]])
y = np.array([1,2])
B = np.array([[1,2], [3,4]])

BMat = matrixOps(A, B)
yMat = matrixOps(A, y)
printMat(BMat.multMat())
printMat(yMat.multMat())
