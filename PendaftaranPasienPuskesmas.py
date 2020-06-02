# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:43:24 2020

@author: User
"""
#standart harga obat= RP10000, standar biaya jasa= RP30000
#standar harga tindakan khusus
   #a. pemberian suntikan = RP20000
   #b. medikasi=RP15000
   #c. penjahitan luka=RP25000
   #d. medikasi kesehatan gigi dan mulut = RP30000
def biaya1(): #obat+jasa
    x1= 10000+30000
    print("Total Biaya: Rp",x1)
    return x1
def biaya2(): #obat+jasa+tindakan khusus a
    x2= 10000+30000+20000
    print("Total Biaya: Rp", x2)
    return x2
def biaya3(): #obat+jasa+tindakan khusus b
    x3= 10000+30000+15000
    print("Total Biaya: Rp", x3)
    return x3
def biaya4(): #obat+jasa+tindakan khusus c
    x4= 10000+30000+25000
    print("Total Biaya: Rp", x4)
    return x4
def biaya5(): #obat+jasa+tindakan khusus a dan b
    x5= 10000+30000+20000+15000
    print("Total Biaya: Rp", x5)
    return x5
def biaya6(): #obat+jasa+tindakan khusus a dan c
    x6= 10000+30000+20000+25000
    print("Total Biaya: Rp", x6)
    return x6
def biaya7(): #obat+jasa+tindakan khusus b dan c
    x7= 10000+30000+15000+25000
    print("Total Biaya: Rp", x7)
    return x7
def biaya8(): #obat+jasa+tindakan khusus a, b, dan c
    x8= 10000+30000+20000+15000+25000
    print("Total Biaya: Rp", x8)
    return x8
def biaya9(): #obat+jasa pelayanan gigi
    x9= 10000+30000
    print("Total Biaya: Rp", x9)
    return x9
def biaya10(): #obat+jasa pelayanan gigi+medikasi kesehatan gigi dan mulut
    x10= 10000+30000+30000
    print("Total Biaya: Rp", x10)
    return x10
def biaya11(): #jasa pelayanan gigi
    x11= 30000
    print("Total Biaya: Rp", x11)
    return x11
listPelayanan= [
               "b1: obat dan jasa",
               "b2: obat, jasa, suntik",
               "b3: obat, jasa, medikasi",
               "b4: obat, jasa, penjahitan luka",
               "b5: obat, jasa, suntik, medikasi",
               "b6: obat, jasa, suntik, jahit luka",
               "b7: obat, jasa, medikasi, jahit luka",
               "b8: obat, jasa, suntik, medikasi, jahit luka",
               "b9: obat dan jasa kesehatan gigi",
               "b10: obat, jasa kesehatan gigi, medikasi",
               "b11: jasa",
               ]
print("PENDAFTARAN PASIEN PUSKESMAS I MOJOSONGO")
print("Jalan Sehat Sejahtera 07, Mojosongo, Solo")
print("======================================================")
print(" ")

print("Silakan Pilih Golongan Pasien")
print("1: Pasien Umum")
print("2: Pasien BPJS")

Z = int(input("Golongan 1 atau 2?: "))
kartu=input("Apakah pasien pernah berobat di sini? (y/t):")
if kartu == "t":
    print("Mohon maaf\nPasien dipersilakan menuju bagian administrasi  untuk mendapatkan nomor rekam medis")  
    print ("Masukkan nomor rekam medis pasien!", end=' ')
    no = input ()
    print ()
else:
    kartu= input("Apakah pasien membawa kartu berobat? (y/t):")
    if kartu == "t" :
        print ("Silakan mencari di data pasien")
        print ("Masukkan nomor kartu berobat pasien!", end=' ')
        no = input ()
         
    else :
        print ("Masukkan nomor kartu berobat pasien!", end=' ')
        no = input ()
        
if Z == 1:
    P = input("Pelayanan P1 atau P2?: ")
    if P == "P1":
        print ("Mohon Tunggu Sebentar, data anda sedang kami proses...")
            
        import time
        time.sleep (5)
        print ()
        print (f"Pasien dengan, \n Golongan         : 1 (Pasien Umum) \nNo. Kartu Berobat : {no} \n====TELAH TERDAFTAR====\nSilakan ambil rekam medis pasien \nPasien dimohon menuju ruang pelayanan umum untuk mendapatkan penanganan\nTerimakasih")
        print("")
        print('')
        print("Rincian Biaya")
        print("Pilih jenis pelayanan")
        print(listPelayanan)
        Q= input("Masukkan pelayanan yang didapatkan pasien!(b1 atau b2 atau dst):")
        if Q== "b1":
            print(biaya1())
        elif Q== "b2":
            print(biaya2())
        elif Q== "b3":
            print(biaya3())
        elif Q== "b4":
            print(biaya4())
        elif Q== "b5":
            print(biaya5())
        elif Q== "b6":
            print(biaya6())
        elif Q== "b7":
            print(biaya7())
        else:
            print(biaya8())
    else:
        print ("Mohon Tunggu Sebentar, data anda sedang kami proses...")
            
        import time
        time.sleep (5)
        print ()
        print (f"Pasien dengan, \n Golongan         : 1 (Pasien Umum) \nNo. Kartu Berobat : {no} \n====TELAH TERDAFTAR====\nSilakan ambil rekam medis pasien \nPasien dimohon menuju ruang pelayanan kesehatan gigi untuk mendapatkan penanganan\nTerimakasih")
        
        print("Rincian biaya")
        print("Pilih jenis pelayanan")
        print(listPelayanan)
        Q= input("Masukkan pelayanan yang didapatkan pasien!(b9 atau b10 atau b11):")
        if Q== "b9":
            print(biaya9())
        elif Q== "b10":
            print(biaya10())
        else:
            print(biaya11())
else:
    print("Masukkan nomor BPJS pasien:", end=' ')
    bpjs= input()
    print()
    P= input("Pelayanan P1 atau P2?: ")
    if P == "P1":
        print ("Mohon Tunggu Sebentar, data anda sedang kami proses...")
    
        import time
 
