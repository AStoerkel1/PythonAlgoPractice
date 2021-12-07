''' 
this is supposed to perform a bunch of operations for matricies
'''

import numpy as np
class leastSquares:
	def __init__(self, A, y):
		self.A = A
		self.y = y
#transpose the matrix		
	def transpose(self, A):
		return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
#multiply matrices
	def mult(self, AT, A):
		return [[sum(a * b for a, b in zip(AT_row, A_col))
				for A_col in zip(*A)]
					for AT_row in AT]	



A = np.array([[1, 2],[3, 4],[5, 6]])

y = np.array([1,3])

Atrans = leastSquares(A, y).transpose(A)


for r in Atrans:
	print(r)

multiple = leastSquares(A, y)

ans = multiple.mult(multiple.transpose(A), A)

for r in ans:
	print(r)

