def insertion_sort(arr,n):
    for i in range(1,n):
        key=arr[i]
        print(i)
        print("go")
        for j in range(i-1,-1,-1):
            print(j)
            if arr[j]>key:
                arr[j+1]=arr[j]

            else:
                arr[j+1]=key
                break




arr=[23,32,4234,234,435,345,3,4,32,5,4,5235,35434,5,345,4,354345,345,3453454,34]
n=len(arr)
insertion_sort(arr,n)
for i in range(n):
    print(arr[i])
