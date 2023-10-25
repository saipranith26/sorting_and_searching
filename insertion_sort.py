def insertion_sort(arr):
    for i in range (1,len(arr)):
        for j in range (i-1,-1,-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [9,8,7,6,5,4,3,2,1,0]
insertion_sort(arr)
print(arr)