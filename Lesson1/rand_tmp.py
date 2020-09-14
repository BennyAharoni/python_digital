from random import randint
from time import sleep

print("Getting random numbers...\n")
sleep(2)
num1 = randint(1, 37)
num2 = randint(1, 37)

if num1 == num2:
    print("You won 100$\n")
else:
    print("You won 0$\n")

print("Bye bye!!")
