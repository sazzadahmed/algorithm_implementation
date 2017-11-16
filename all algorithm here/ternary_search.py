def binarry_search(arr,low,high,search_element):
    if low>high:
        return -1
    else:
        mid=(high+low)/2
        print(mid)
        if arr[mid]==search_element:
            return mid
        else:
            if arr[mid]>search_element:
                high=mid-1
            else:
                low=mid+1
            return binarry_search(arr,low,high,search_element)
def ternary_search(arr,low,high,search_element):
    if low>high:
        return -1
    mid1=low+(high-low)/3
    mid2=+mid1+(high-low)/3
    if arr[mid1]==search_element:
        return mid1
    if arr[mid2]==search_element:
        return mid2
    if search_element<arr[mid1]:
        return ternary_search(arr,low,high=mid1-1)
    if search_element>arr[mid2]:
        return ternary_search(arr,mid2+1,high,search_element)
    return ternary_search(ar,mid1+1,mid2-1,search_element)

arr=[i for i in range(1,100,1) if not i%2]
n=98
p=ternary_search(arr,0,len(arr),98)
print(arr[p])


