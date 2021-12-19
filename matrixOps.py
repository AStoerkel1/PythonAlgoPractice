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
	def multMat(self, A, B):
#B is a matrix
		if type(B[0]) is (np.ndarray):
			return [[sum(a * b for a, b in zip(A_row, B_col))for B_col in zip(*B)]for A_row in A]
#B is a vector
		else:
			return [sum(a * b for a, b in zip(A_row, self.B)) for A_row in self.A]

#given a matrix and vector that are inconsistant, this will find the least squares solution
	def leastSquares(self):
		ATrans = self.transpose()
		AtA = self.multMat(ATrans, self.A)
		AtB = self.multMat(ATrans, self.B)
		return np.linalg.solve(AtA, AtB)

def printMat(A):
	for i in A:
		print(i)

#this is a test
A = np.array([[1, 1],[1,2]])
B = np.array([2,2])

BMat = matrixOps(A, B)
print(BMat.leastSquares())
