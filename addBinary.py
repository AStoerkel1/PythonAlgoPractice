#add two binary strings
def addBinary(a: str, b: str) -> str:
    #y is the shorter list (Addend)
    #x is the longer list (Augend)
    if len(a) <= len(b):
        y = list(a)
        x = list(b)
    else:
        x= list(a)
        y = list(b)
    #create pointers j: x, i: y
    j = -1
    i = -1
    #while the addend pointer is 
    #within range from back to front
    while i >= -(len(y)):
        #if the addend is zero do nothing
        #advance pointers
        if y[i] == '0':
            j -= 1
            i -= 1
        #if the augend is 0 and addend is 1
        #add 1 to that digit
        #advance pointers
        elif x[j] == '0':
            x[j] = '1'
            j-=1
            i-=1
        #augend is 1 and addend is 1
        else:
            #while augend is still 1
            while x[j] == '1':
                #make the augend 0
                x[j] = '0'
                #if we made the highest order digit 0
                if j == -(len(x)):
                    #carry the one to the front
                    x = ['1'] + x
                    #advance the augend pointer
                    j-=1
                    #break the loop
                    break
                #advance the augend pointer inside the carry loop
                j-=1
            #broke out of the loop when augend digit is 0
            #make 0 digit a 1
            x[j] = '1'
            #make sure augend pointer is reset to proper digit
            j=i-1
            #advance addend pointer
            i-=1
    return ''.join(x)
print(addBinary('110', '0'))