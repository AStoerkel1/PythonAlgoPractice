from check_prime import check_p, divisors
prime_facts = []

def GPF(p):
    b = divisors(p)
    print (b)
    b.sort()   
    print (b)
    c = []
    
    
    #something is fucky here
    for j in b:
        if check_p(j)==True:
            c.append(j)
            print(c)
        
    return c

print(GPF(91))
