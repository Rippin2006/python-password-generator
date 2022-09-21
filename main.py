import numbers
import random

uppercase_letters = "ABCDEFGHIJKMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
number = "1234567890"
symbol = "()[]{},;.!@#$%^&*"

upper, lower, num, sym = True, True, True, True

all = ""

if upper:
    all = all + uppercase_letters
if lower:
    all = all + lowercase_letters
if num:
    all = all + number
if sym:
    all = all + symbol
    
length = 8
amount = 10

for i in range(amount):
    password ="".join(random.sample(all, length))
    print(password)