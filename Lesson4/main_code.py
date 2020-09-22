from time import sleep #we can also write from time import *
from random import randint
from Lesson4.defim import menu, calculating, dogs_age

#sleep(3)
#if we write import time, we have to write time.sleep(3)

menu()
sleep(2)
print("Wow!\n\n")
calculating(3, 6)
dogs_age(int(input("Enter dog's age: ")))
