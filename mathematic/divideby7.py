'''
A number can be divided 3 if the  if the absolute different of even and odd bit will multiple of 3
'''
def SevenMultiple(x):
    y=(x<<3)-x
    return y
def multiple_of_three(x):
    even=0
    odd=0
    flag=False
    while(x):
        if(x%2):
            if (flag):
                even=even+1
                flag=False
            else:
                odd=odd+1
                flag=True
        else:
            flag=not flag
        x=x/2
        #print(even, ' ', odd)
    print(even,' ',odd)

a=SevenMultiple(10)
b=multiple_of_three(11)
print(a)

