

#check_prime

from math import sqrt
nums = []
def divisors(n):
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            nums.append(i)
            if i * i != n:
                nums.append(n // i)
    print(nums)
    return nums


def check_p(n):
    a = len(divisors(n))
    if a == 2:
        return True
    else:
        return False

print(check_p(91))
