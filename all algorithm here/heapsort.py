def heapify(arr,i,n):
    '''
    this is simple max heap code
    :param arr:
    :param i:
    :param n:
    :return:
    '''
    largest=i
    left=2*i
    right=2*i+1
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if i!=largest:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,largest,n)



def heap_sort(arr,n):
    '''
    this is simple headsort code implementation
    here a given array first heapfy it into max heap
    then swap the last element and descrese it size again
     with root and heapfy it again
    and then continue this process untill full sort
    :param arr:
    :param n:
    :return:
    '''
    for i in range(n/2,-1,-1):
        heapify(arr,i,n)
    for i in range(n-1,-1,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,0,i)

arr=[1,2,1,3,52354,23,241,5445,465,456,3532,52334,3,3,546,34,2,1,5,34,12,34]
n=len(arr)
heap_sort(arr,n)

for i in range(n):
    print(arr[i],' ')