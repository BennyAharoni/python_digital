from random import randint
from time import sleep

print("Welcome to our Cube game\nEach torn cost 3 ILS")
money = int(input("Enter how much money do you have? "))
turns = money//3
print("You have: " + str(turns) + " turns\nYour change: " + str(money % 3) + " ILS\n")
prize = 0

for i in range(turns):
    print("Rolling Cubes for Round Number " + str(i + 1) + " :\n----------------")
    sleep(1)
    cube1 = randint(1, 6)
    cube2 = randint(1, 6)
    print("Cube 1: " + str(cube1) + "\nCube 2: " + str(cube2) + "\n")

    if(cube1 == cube2):
        if(cube1 == 6):
            prize += 1000
        else:
            prize += 100
    elif(cube1 == 1):
        prize += 20
    elif(cube2 == 2):
        prize += 40

print("Calculating your prize...")
sleep(2)
print("Your prize: " + str(prize))