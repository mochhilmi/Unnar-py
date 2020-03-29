def swap(teh,kopi):
    susu = kopi
    kopi = teh
    teh = susu
    return(teh,kopi)

awal = input("masukkan iputan awal : ")
akhir = input("masukkan inputan akhir : ")

print ("\ninputan awal : ", awal)
print ("inputan akhir : ", akhir)

awal, akhir = swap(kopi=akhir, teh=awal)

print("\ninputan setelah swap : ")
print("nilai awal : ",awal, "\nnilai akhir : ",akhir)

