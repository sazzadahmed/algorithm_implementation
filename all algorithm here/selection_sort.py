arr=[1,2,4,32,42323,4234,2,34,2,3,4,23,4,23,4]
for i in range(len(arr)):
    mn=i
    for j in range(i,len(arr)):
        if arr[j]<arr[mn]:
            mn=j

    arr[i],arr[mn]=arr[mn],arr[i]
for i in range(len(arr)):
    print(arr[i])



'''
bubble sort here
'''
arr=[i for i in range(100,1,-1)]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(len(arr)):
    print (arr[i])
