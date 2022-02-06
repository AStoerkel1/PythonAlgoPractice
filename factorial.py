#simple function to find a factorial
def n_factorial(n):
    ans=1
    while n >0:
        ans*=n
        n-=1
    return ans
