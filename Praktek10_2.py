def BubbleSort(arr, x):
    if x <= 1:
        return arr
    
    for y in range(x-1):
        if arr[y] > arr[y+1]:
            arr[y], arr[y+1] = arr[y+1], arr[y]
            
    return BubbleSort(arr, x -1)

lis = [10, 32, 64, 14, 7, 13, 23]
print(BubbleSort(lis, len(lis))) 