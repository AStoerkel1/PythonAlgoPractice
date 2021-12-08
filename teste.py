#test some compositional statements
''' 
1 2
3 4
5 6

into 

1 3 5
2 4 6

notation: A[row][col]
	  A[outer][inner]
'''
A = [[1,2], [3,4], [5,6]]
B = [[1, 2],[3,4]]

newLs = [[A[i][j] for i in range(len(A))]for j in range(len(A[0]))]

for A_row in A:
	for B_col in zip(*B):
		print([sum(a * b for a, b in zip(A_row, B_col))])

