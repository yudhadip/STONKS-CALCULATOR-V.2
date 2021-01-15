from numpy import arange
import sys

print("STONKS CALCULATOR")
error = "Please input the correct value (number only)"
input_list = []

def value_checker(self):
    try:
        list(map(float, input_list))
    except ValueError:
        print(error)
        sys.exit()


x = (input("Your initial asset : "))
input_list.append(x)
value_checker([0])

b1 = (input("Expected profit percentage (%) for each trades: "))
input_list.append(b1)
value_checker([1])

limit_max = (input("The amount of trades you will made this month: "))
input_list.append(limit_max)
value_checker([2])


x = float(x)
b1 = float(b1)
limit_max = float(limit_max)
og_tuple = (x, b1, limit_max)
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

print("Your stonks after ", int(limit_max),"amount of trades are:", total)
print("Congratulations!, you have made",total - og_tuple[0], "profit, which is ",
      int(((total - og_tuple[0]) / og_tuple[0]) * 100),"% of your initial assets!")
