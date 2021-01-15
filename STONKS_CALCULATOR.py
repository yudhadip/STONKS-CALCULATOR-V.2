from numpy import arange
import sys

print("STONKS CALCULATOR")
error = "Please input the correct value (number only)"

def value_checker1(self):
    try:
        float(x)
    except ValueError:
        print(error)
        sys.exit()

def value_checker2(self):
    try:
        float(b1)
    except ValueError:
        print(error)
        sys.exit()

def value_checker3(self):
    try:
        float(limit_max)
    except ValueError:
        print(error)
        sys.exit()

x = (input("Your initial asset : "))
value_checker1(x)

b1 = (input("Expected profit percentage (%) for each trades: "))
value_checker2(b1)

limit_max = (input("The amount of trades you will made this month: "))
value_checker3(limit_max)

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
    print("Compound interest after each trades: ", total)

str(limit_max)

print("Your stonks after ", limit_max,"amount of trades are:", total)
