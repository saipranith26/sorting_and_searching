def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[i],arr[j] = arr[j],arr[i]

arr= [9,8,7,6,5,4,3,2,1,0]
bubble_sort(arr)
print(arr)