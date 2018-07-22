#returns all even fib sequence up to 4 mil and their sum

def even_fib(upperbound):
    a = 1
    b = 2
    ans = 0
    while b < upperbound:
        b = a + b
        a = b - a
        if a % 2 ==0:
            print(a)
            ans+=a
    return ans
print(even_fib(4000000))