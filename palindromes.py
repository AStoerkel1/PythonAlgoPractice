'''A palindromic number reads the same both ways. The largest palindrome made from
 the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers'''

from pals import is_pal

def largest_palidrome_product(n_digit_numbers):
    lower_bound = 10 ** (n_digit_numbers - 1)
    upper_bound = lower_bound * 10
    return max(
            map(int,
            filter(is_pal, (str(int(i * j)) 
            for i in range(lower_bound, upper_bound) 
            for j in range(i, upper_bound)))))

def p1():
    return largest_palidrome_product(3)


if __name__ == '__main__':
    assert 9009 == largest_palidrome_product(2)
    answer = p1()
print("max palindrome: {}".format(answer))