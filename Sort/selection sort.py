import time

angka = [3, 40, 20, 53, 21, 56]
print("Selection sort")
print("\narray awal : ", angka)
print()
start = time.time()

for awal in range(len(angka)-1):
    akhir = awal

    for x in range(awal+ 1, len(angka)):
        if angka[awal] > angka[x]:
            akhir = x

    angka[akhir], angka[awal] = angka[awal],angka[akhir]
    print ("proses ke -",(awal+1), angka)

end = time.time()
print()
print("array akhir :", angka)
print("Selesai dalam %f detik" % (end - start))


