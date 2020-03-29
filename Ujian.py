from time import time
from re import match
from random import randint

def Input():
    global pilihan,data
    while pilihan != 4:
        print('\nPisahkan hanya dengan Spasi!')
        print('Silahkan dikosongi untuk data acak')
        data = input('Masukkan data angka\t: ')
        if data is '':
            data = [randint(0, 100) for a in range (0,randint(3,6))]
            menu()
        elif data is not '':
            if match('(?=\d+)[\d\s]+$',data):
                data = data.split()
                menu()
            else:
                print("\033[91m {}\033[00m".format('\ndata hanya bisa berisi angka, dan dipisah hanya dengan Spasi !'))

def menu():
    global pilihan
    while pilihan != 4:
        print('\nData awal\t:',data)
        print('\nPilih Menu\n')
        print('1. Selecton Sort')
        print('2. Bubble Sort')
        print('3. Ubah data')
        print('4. Keluar')
        pilihan = input('Masukkan nomor pilihan disini\t: ')
        print()
        if pilihan.isnumeric():
            pilihan = int(pilihan)
            if pilihan == 1:
                print('Data awal\t:',data)
                print()
                Selection()
            elif pilihan == 2:
                print('Data awal\t\t:',data)
                print()
                Bubble()
            elif pilihan == 3:
                Input()
            elif pilihan == 4:
                break
            else:
                print("\033[91m{} {}\033[00m".format('Tidak ada pilihan No',pilihan))
        else:
            print("\033[91m{} {}\033[00m".format('Tidak ada pilihan No',pilihan))

def Selection():
    Data = data
    start = time()
    for b in range (len(Data)-1):
        min = b
        for c in range (b+1,len(Data)):
            if int(Data[min]) > int(Data[c]):
                min = c
        d = Data[b]; Data[b] = Data[min]; Data[min] = d
        print('proses ke - ',(b+1),'\t:',Data)

    print()
    print('Data Akhir\t:',Data)
    end = time()
    print('\nselesai dalam waktu\t:{:f} Detik'.format(end-start))

def Bubble():
    Data = data
    start = time()
    for b in range (len(Data)):       
        for c in range (0,len(Data)-b-1):
            if int(Data[c]) > int(Data[c+1]):
                d = Data[c]; Data[c] = Data[c+1]; Data[c+1] = d
            print('proses ke -',(b+1,c+1),'\t:',Data)
    print()
    print('Data Akhir\t\t:',Data)
    end = time()
    print('\nselesai dalam waktu\t: {:f} Detik'.format(end-start))

print('-'*28)
print('Nama\t: Moch Hilmi\nNIM\t: 04319032')
print('-'*28)

pilihan = 0

Input()