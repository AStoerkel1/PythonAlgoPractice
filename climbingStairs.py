#You are climbing a staircase. It takes n steps to reach the top
#Each time you can either climb 1 or 2 steps. In how many distinct 
#ways can you climb to the top?


'''
n=2
output = 2
1. 1 step + 1 step
2. 2 steps

n=3
output = 3
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
#this returns the correct answer but takes too long
#def climbStairs(n: int) -> int:
#    
#    if(n == 1):
#        return 1
#    elif(n == 2):
#        return 2
#    else:
#        return climbStairs(n-1)+climbStairs(n-2)

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n==2:
        return 2

    fibs = [0]*(n)
    fibs[0] = 1
    fibs[1] = 2
    for i in range(2, n):
        fibs[i] = fibs[i-1]+fibs[i-2]
    return fibs[n-1]

print(climbStairs(45))
