
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("error occured ValueError")

try:
    result = x / y
    print(f"{x} / {y} = {result}")
except ZeroDivisionError:
    print("error occured ZeroDivisionError")