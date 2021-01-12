from numpy import arange
import sys
import re

print("STONKS CALCULATOR")

x = (input("masukan modal: "))

try:
    float(x)
except ValueError:
    print("yang dimasukin angka tolol bukan lu?")
    sys.exit()

b1 = (input("masukan jumlah persen yang diinginkan (%): "))

try:
    float(b1)
except ValueError:
    print("yang dimasukin angka tolol bukan lu?")
    sys.exit()

limit_max = (input("masukan jumlah hari yang diinginkan: "))

try:
    float(limit_max)
except ValueError:
    print("yang dimasukin angka tolol bukan lu?")
    sys.exit()

x = float(x)
b1 = float(b1)
limit_max = float(limit_max)
b2 = 100
total = 0
limit_min = 1
z = x * (b1 / b2)
step = 1
a = 1

for total in arange(limit_min, limit_max, step):
    total += (x + z) - a
    x = total
    z = x * (b1 / b2)
    a += 1
    print(total)
