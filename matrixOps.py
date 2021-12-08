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
#multiply matrix by it's transpose
	def transMult(self, AT, A):
		return [[sum(a * b for a, b in zip(AT_row, A_col))
				for A_col in zip(*A)]
					for AT_row in AT]	


A = np.array([[1, 2],[3, 4],[5, 6]])

y = np.array([1,3])

multiple = matrixOps(A, y)

Atrans = multiple.transpose(A)

for r in Atrans:
	print(r)

ans = multiple.transMult(Atrans, A)

for r in ans:
	print(r)



