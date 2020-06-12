# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:43:24 2020

@author: User
"""

import csv
O = 10000 #standart harga obat
J= 30000 #standart biaya jasa
Ta= 20000 #standart biaya tindakan khusus a (pemberian suntikan)
Tb= 15000 #standart biaya tindakan khusus b (medikasi)
Tc= 25000 #standart biaya tindakan khusus b (penjahitan luka)
Td= 30000  #standart biaya tindakan khusus d (medikasi kesehatan gigi dan mulut)
Tbpjs= 0

def biaya1(): #obat+jasa
    x1= O + J
    return x1
def biaya2(): #obat+jasa+tindakan khusus a
    x2= O + J + Ta
    return x2#"Anda menggunakan layanan NON-BPJS"
def biaya3(): #obat+jasa+tindakan khusus b
    x3= O + J + Tb
    return x3 #"Anda menggunakan layanan NON-BPJS"
def biaya4(): #obat+jasa+tindakan khusus c
    x4= O + J + Tc
    return x4 #"Anda menggunakan layanan NON-BPJS"
def biaya5(): #obat+jasa+tindakan khusus a dan b
    x5= O + J + Ta + Tb
    return x5 # "Anda menggunakan layanan NON-BPJS"
def biaya6(): #obat+jasa+tindakan khusus a dan c
    x6= O + J + Ta + Tc
    return x6 #"Anda menggunakan layanan NON-BPJS"
def biaya7(): #obat+jasa+tindakan khusus b dan c
    x7= O + J + Tb +Tc
    return x7 #"Anda menggunakan layanan NON-BPJS"
def biaya8(): #obat+jasa+tindakan khusus a, b, dan c
    x8= O + J + Ta + Tb +Tc
    return x8 # "Anda menggunakan layanan NON-BPJS"
def biaya9(): #obat+jasa pelayanan gigi
    x9= O + J
    return x9 #"Anda menggunakan layanan NON-BPJS"
def biaya10(): #obat+jasa pelayanan gigi+medikasi kesehatan gigi dan mulut
    x10= O + J + Td
    return x10 #"Anda menggunakan layanan NON-BPJS"
def biaya11(): #jasa pelayanan gigi
    x11= J
    return x11 #"Anda menggunakan layanan NON-BPJS"
def biaya00(): #Pengguna Layanan BPJS
    x00= Tbpjs
    return x00 #"Anda menggunakan layanan BPJS"

print("======================================================")
print("|     PENDAFTARAN PASIEN PUSKESMAS I MOJOSONGO       |")
print("|    Jalan Sehat Sejahtera 07, Mojosongo, Solo       |") 
print("======================================================")
print(" ")

import datetime
time = datetime.datetime.now()
waktu=time
print(waktu)

print("")
print("")
print("SILAHKAN ISI DENGAN PILIHAN YANG TERTERA")
print("")
print("ketik [y] untuk ya")
print("ketik [t] untuk tidak")
print("")

valid = 0;
while (valid != 1):
    kartu=input("Apakah pasien pernah berobat di sini? (y/t):")
    if kartu == "t":
        print("Mohon maaf\nPasien dipersilakan menuju bagian administrasi  untuk mendapatkan nomor rekam medis")  
        print ("Masukkan nomor rekam medis pasien!", end=' ')
        no = input ()
        print ()
        valid = 1;
            
    elif kartu == "y":
        while (valid !=1):
            kartu= input("Apakah pasien membawa kartu berobat? (y/t):")
            if kartu == "t" :
                print ("Silakan mencari di data pasien")
                print ("Masukkan nomor kartu berobat pasien!", end=' ')
                nomor = input ()
                valid = 1;
            elif kartu == "y" :
                f= open('DataPasien.txt', 'r')
                reader= csv.reader(f)
                pasien = {}
                for row in reader:
                    pasien[row[0]] = {'nama': row[1], 'alamat' : row[2], 'golongan' : row[3]}
                nomor = input("Masukkan nomor kartu berobat pasien!")
                test = nomor
                print("")
                print("Data Pasien")
                print("Nomor Rekam Medis Pasien : ",nomor)
                print("Nama                     : ", pasien[nomor]['nama'])
                print("Alamat                   : ", pasien[nomor]['alamat'])
                print("Golongan Pasien          : ", pasien[nomor]['golongan'])
                valid = 1;
            else:
                print ("Silahkan masukan pihihan [y] atau [t]")
            
    else:
        print ("Silahkan masukan pihihan [y] atau [t]")
        
print("")       
print("SILAHKAN PILIH GOLONGAN PASIEN")
print("Ketik [1] untuk PASIEN UMUM")
print("Ketik [2] untuk PASIEN BPJS")
        
while True:
    try:
        Z = int(input("Golongan 1 atau 2?: "))
        if Z == 1:
            print ("")
            print ("SILAHKAN PILIH PELAYAN")
            print ("ketik [P1] untuk PELAYANAN UMUM")
            print ("ketik [P2] untuk PELAKANAN KESEHATAN GIGI & MULUT")
            while True:
                P = input("Pelayanan P1 atau P2?: ")
                if P == "P1":
                    print ("Mohon Tunggu Sebentar, data anda sedang kami proses...")
                
                    import time
                    time.sleep (5)
                    print ()
                    print (f"Pasien dengan, \n Golongan         : 1 (Pasien Umum) \nNo. Kartu Berobat : {nomor} \nDipersilakan ambil rekam medis pasien \nPasien dimohon menuju ruang pelayanan umum untuk mendapatkan penanganan\nTerimakasih")
                    print("")
                    print('')
                    print("Rincian Biaya")
                    
                    while True:
                        print(f"__________________________________________________")
                        print(f"========== SILAHKAN PILIH PELAYANAN ==============|")
        print (f"Pasien dengan, \n Golongan         : 1 (Pasien Umum) \nNo. Kartu Berobat : {no} \n====TELAH TERDAFTAR====\nSilakan ambil rekam medis pasien \nPasien dimohon menuju ruang pelayanan kesehatan gigi untuk mendapatkan penanganan\nTerimakasih")
        
        print("Rincian biaya")
        print(f"__________________________________________________")
        print(f"|========== SILAHKAN PILIH PELAYANAN ==============|")
        print(f"__________________________________________________")
        print(f"|  B9.  obat dan jasa kesehatan gigi              |")
        print(f"|  B10. obat, jasa kesehatan gigi, medikasi       |")
        print(f"|  B11. jasa                                      |")
        print(f"-------------------------------------------------")
        pilih_layanan = input("Pilih layanan (B9-B11) : ")
        if pilih_layanan == "B9":
            print(biaya9())
        elif pilih_layanan == "B10":
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
        time.sleep (5)
        print ()
        print (f"Pasien dengan, \n Golongan         : 2 (Pasien BPJS) \nNo. Kartu Berobat : {no} \nNo. Kartu BPJS    : {bpjs} \n====TELAH TERDAFTAR====\nSilakan ambil rekam medis pasien \nPasien dimohon menuju ruang pelayanan umum untuk mendapatkan penanganan\nTerimakasih")
        print("")
        print('')
        print("Rincian Biaya")
        print(f"__________________________________________________")
        print(f"========== SILAHKAN PILIH PELAYANAN ==============|")
        print(f"__________________________________________________")
        print(f"|  B1.  obat dan jasa                             |")
        print(f"|  B2.  obat, jasa, suntik                        |")
        print(f"|  B3.  obat, jasa, medikasi                      |")
        print(f"|  B4.  obat, jasa, penjahitan luka               |")
        print(f"|  B5.  obat, jasa, suntik, medikasi              |") 
        print(f"|  B6.  obat, jasa, suntik, jahit luka            |")
        print(f"|  B7.  obat, jasa, medikasi, jahit luka          |")
        print(f"|  B8.  obat, jasa, suntik, medikasi, jahit luka  |")
        print(f"-------------------------------------------------")
        pilih_layanan = input("Pilih layanan (B1-B8) : ")
        if pilih_layanan == "B1":
            print(biaya00())
        elif pilih_layanan == "B2":
            print(biaya00())
        elif pilih_layanan == "B3":
            print(biaya00())
        elif pilih_layanan == "B4":
            print(biaya00())
        elif pilih_layanan == "B5":
            print(biaya00())
        elif pilih_layanan == "B6":
            print(biaya00())
        elif pilih_layanan == "B7":
            print(biaya00())
        else:
            print(biaya00())     
     
    else:
         print ("Mohon Tunggu Sebentar, data anda sedang kami proses...")
            
         import time
         time.sleep (5)
         print ()
         print (f"Pasien dengan, \n Golongan         : 2 (Pasien BPJS) \nNo. Kartu Berobat : {no} \nNo. Kartu BPJS    : {bpjs} \n====TELAH TERDAFTAR====\nSilakan ambil rekam medis pasien \nPasien dimohon menuju ruang pelayanan kesehatan gigi untuk mendapatkan penanganan\nTerimakasih")
         print("__________________________________________________")
         print(f"|========== SILAHKAN PILIH PELAYANAN ==============|")
         print("__________________________________________________")
         print(f"|  B9.  obat dan jasa kesehatan gigi              |")
         print(f"|  B10. obat, jasa kesehatan gigi, medikasi       |")
         print(f"|  B11. jasa                                      |")
         print(f"-------------------------------------------------")
         pilih_layanan = input("Pilih layanan (B9-B11) = ")
         if pilih_layanan == "B9":
            print(biaya00())
         elif pilih_layanan == "B10":
            print(biaya00())
         else:
            print(biaya00())
print("")
print("Pembayaran dilakukan di bagian kasir.")
print("")
print("Peroses telah selesai")

 
