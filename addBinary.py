#add two binary strings
def addBinary(a: str, b: str) -> str:
    if len(a) <= len(b):
        y = list(a)
        x = list(b)
    else:
        x= list(a)
        y = list(b)
    
    j = -1
    i = -1
    while i >= -(len(y)):
        if y[i] == '0':
            j -= 1
            i -= 1
            continue
        elif x[j] == '0':
            x[j] = '1'
            j-=1
            i-=1
            continue
        else:
            while x[j] == '1':
                x[j] = '0'
                if j == -(len(x)):
                    x = ['1'] + x
                    j-=1
                    break
                j-=1
                
            x[j] = '1'
            j=i-1
            i-=1
    return ''.join(x)
print(addBinary('110', '111'))