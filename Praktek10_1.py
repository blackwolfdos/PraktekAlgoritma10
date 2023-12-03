def BinarySearch(array, start, end, x):
    if end >= start:
        y = start + (end - start) // 2
        if array[y] == x:
            return y
        elif array[y] > x:
            return BinarySearch(array, start, y -1, x)
        else:
            return BinarySearch(array, y + 1, end, x)
    else:
        return -1
    
def BubbleSort(array):
    for x in range(len(array)-1):
        for y in range(0, len(array)-x-1):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
                
    angka = int(input("Angka yang di cari: "))
    print("Setelah BubbleSort: ",array)
    hasil = BinarySearch(array, 0, len(array)-1, angka)
    
    if hasil != -1: 
        print ("Elemen ditemukan pada posisi ke-" + str(hasil+1))
    else: 
        print ("Elemen tidak ditemukan pada list")
        
array = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
BubbleSort(array)