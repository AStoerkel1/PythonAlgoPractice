''' 
this is supposed to perform a bunch of operations for matricies
'''

import numpy as np
class matrixOps:
#A = any matrix, y = a multiplicable vector
	def __init__(self, A, y):
		self.A = A
		self.y = y

#transpose the matrix		
	def transpose(self, A):
		return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

#multiply matricies (ngl i have no idea how this works i found it online)
	def transMult(self, A, B):
		return [[sum(a * b for a, b in zip(A_row, B_col))
				for B_col in zip(*B)]
					for A_row in A]	

#solve a system of equations (unfortunately the matrix has to be square
	def leastSquares(self):
		Atrans = self.transpose(self.A)
		ATA = self.transMult(Atrans, A)
		return np.linalg.inv(ATA).dot(self.y)

A = np.array([[1, 2],[3, 4],[5,6]])

y = np.array([1,3])

multiple = matrixOps(A, y)

print(multiple.leastSquares())

