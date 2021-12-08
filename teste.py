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
ls = [[1,2], [3,4], [5,6]]


newLs = [[ls[i][j] for i in range(len(ls))]for j in range(len(ls[0]))]

print(newLs)
print(ls[0][1])
