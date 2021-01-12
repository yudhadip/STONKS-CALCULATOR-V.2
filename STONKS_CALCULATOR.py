import numpy
print("STONKS CALCULATOR")
x = float(input("masukan modal: "))
b1 = float(input("masukan jumlah persen yang diinginkan (%): "))
b2 = 100
z = x * (b1 / b2)
total = 0
limit_min = 1
limit_max = float(input("masukan jumlah hari yang diinginkan: "))
step = 1
a = 1

for total in numpy.arange(limit_min, limit_max, step):
    total += (x + z) - a
    x = total
    z = x * (b1 / b2)
    a += 1
    print(total)
