''' 
this is supposed to perform a bunch of operations for matricies

'''

import numpy as np
class matrixOps:
#A = any matrix, y = a multiplicable vector or matrix
	def __init__(self, A, y):
		self.A = A
		self.y = y

#transpose the matrix		
	def transpose(self, A):
		return [list(x) for x in zip(*A)]

#multiply matricies (i found the mat*mat alg online but modified it for vectors)
	def multMat(self, A, B):
#B is a matrix
		if type(B[0]) is (np.ndarray):
			return [[sum(a * b for a, b in zip(A_row, B_col))for B_col in zip(*B)]for A_row in A]
#B is a vector
		else:
			return [sum(a * b for a, b in zip(A_row, B)) for A_row in A]

#solve a system of equations (unfortunately the matrix has to be square)
	def leastSquares(self):
		Atrans = self.transpose(self.A)
		ATA = self.multMat(Atrans, A)
		return np.linalg.inv(ATA).dot(self.y)

A = np.array([[1, 2],[3, 4],[5,6]])

y = np.array([[1,2], [3,4]])

multiple = matrixOps(A, y)

print(multiple.multMat(A, y))
print(multiple.multMat(A, y[0]))
