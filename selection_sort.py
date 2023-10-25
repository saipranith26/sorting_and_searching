def selection_sort(arr):
    for i in range(len(arr)):
        min_val = i
        for j in range(i+1, len(arr)):
            if arr[min_val] > arr[j]:
                min_val = j
        arr[i],arr[min_val] =arr[min_val],arr[i]
arr= [9,8,7,6,5,4,3,2,1,0]
selection_sort(arr)
print(arr)