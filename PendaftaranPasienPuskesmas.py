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

