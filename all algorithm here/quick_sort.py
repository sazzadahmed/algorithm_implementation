def partition(arr,low,high):
    i=low-1
    for j in range(low,high):
        if arr[j]<=arr[high]:
            i=i+1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i
def Quicksort(arr,low,high):
    if low<high:
        partitionIndex=partition(arr,low,high)
        Quicksort(arr,low,partitionIndex)
        Quicksort(arr,partitionIndex+2,high)
        return
    else:
        return
arr=[1,2,3,4,5,4,3,2,3,34523434,344,4253,345,5354235,5,345,3254235455,546,657]
sz=len(arr)
Quicksort(arr,0,sz-1)
for i in range(sz):
    print(arr[i])