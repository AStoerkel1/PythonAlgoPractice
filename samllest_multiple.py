'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
from factorial import n_factorial



def Funky(UB):
    a = int(n_factorial(UB))
    for i in range(2520, a, 20):
        j = UB-1
        while i % j ==0:
            if j==1:
                return i    
            j-=1

##print(Funky(20))