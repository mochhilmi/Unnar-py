def binarySearch(arr, l, r, x):

    while l <= r:

        tengah = l + ((r - l) // 2)

        if arr[tengah] == ygdicari:
            return tengah

        elif arr[tengah] < ygdicari:
            l = tengah + 1

        else:
            r = tengah - 1

    return False


arr = [2, 3, 4, 10, 40]
ygdicari = 40

result = binarySearch(arr, 0, len(arr) - 1, ygdicari)

if result:
    print("Elemen yang dicari ada di index ke", result)
else:
    print("Elemen yang dicari tidak ada dalam array")