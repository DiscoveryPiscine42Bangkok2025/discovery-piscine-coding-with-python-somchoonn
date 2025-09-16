def array_first():
    newarr = []
    arr = [2,8,9,48,8,22,-12,2]
    print(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] + 2
    for i in range(len(arr)):
        if arr[i] > 5:
            newarr.append(arr[i])
    print(newarr)
array_first()