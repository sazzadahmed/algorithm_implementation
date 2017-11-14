def merge(arr,strt,mid,endd):
    lst=[]
    lst1=[]
    for i in range(strt,mid+1):
        lst.append(arr[i])
    for i in range(mid+1,endd+1):
        lst1.append(arr[i])
    i=len(lst)-1
    j=len(lst1)-1
    k=endd
    while i >=0 and j>=0:
        if lst[i]>lst1[j]:
            arr[k]=lst[i]
            i=i-1
        else:
            arr[k]=lst1[j]
            j=j-1
        k=k-1


    if i<0:
        while j>=0:
            arr[k]=lst1[j]
            j=j-1
            k=k-1
    else:
        while i>=0:
            arr[k]=lst[i]
            i=i-1
            k=k-1

    #return arr


def merge_sort(arr,strt,endd):
    if strt==endd:
        return
    mid=(strt+endd)/2
    merge_sort(arr,strt,mid)
    merge_sort(arr,mid+1,endd)
    arr=merge(arr,strt,mid,endd)
    return;


arr=[1,2,4,32,42323,4234,0,0,0,0,0,0,2,34,2,3,4,23,4,23,4]
size=len(arr)
merge_sort(arr,0,size-1)
for i in range(0,size):
    print (arr[i])