from math import sqrt
def divisors_gen(n):
    divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    print (len(divisors))
    return divisors