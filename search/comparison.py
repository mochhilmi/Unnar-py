import time


print("-" * 20)
print("Nama\t: Moch Hilmi\nNIM\t: 04319032")
print("-" * 20)

def kondisi(l,b):
    if l == b:
        print("\nElemen di temukan di index ke", l)
        print('Linear Search\t: ditemukan dalam %f detik' %waktuliniear)
        print('binary Search\t: ditemukan dalam %f detik' %waktubinary)
    elif (l == True) and (b == False):
        print('\nLinear Search\t: ditemukan di index ke %d, dalam waktu %f detik' %(l,waktuliniear))
        print('\nDalam algoritma Binary Search array harus sudah di urutkan')
    else:
        print("\nElemen yang dicari tidak ada dalam array")



def binarySearch(arr, l, r, x):

    while l <= r:
        tengah = l + ((r - l) // 2)
        if arr[tengah] == x:
            return tengah
        elif arr[tengah] < x:
            l = tengah + 1
        else:
            r = tengah - 1

    return False


def linierSearch(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i

    return False


array = [5, 10, 20, 23, 34, 75, 100]
ygdicari = 34
print('\nArraynya\t\t:',array)
print('Elemen yang dicari\t:',ygdicari)

start = time.time()
linear = linierSearch(array, len(array), ygdicari)
end = time.time()
waktuliniear = end-start

start = time.time()
binary = binarySearch(array, 0, len(array)-1, ygdicari)
end = time.time()
waktubinary = end-start

kondisi(linear,binary)
