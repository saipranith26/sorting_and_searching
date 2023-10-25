def linear_search(arr,tar):
    for i in arr:
        if i ==  tar :
            return tar
    return -1
arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tar= 20
print(linear_search(arr,tar))