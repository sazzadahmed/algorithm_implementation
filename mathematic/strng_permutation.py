'''
python string permutaion code

'''
def permutation(a):
    b=[]
    print (a)
    if len(a)==1:
        b+=[a]
    for i,v in enumerate(a):
        '''
        the Idea behind it is pretty simple  in every iteration for given string i character comes first
        and  send to other string to recursive permutation
        '''
        pre=a[:i]+a[i+1:]
        for j in permutation(pre):
            '''
                permutated list is gotten here now add the code here
            '''
            b+=[v+j]

    return b

a=permutation('abcd')
print(a)