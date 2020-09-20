from time import sleep

for x in range(1, 10): # prints 1-9
    print(x)

list_fruit = ["banana", "apple", "orange"]
for x in list_fruit:
    print(x)

for x in range(len(list_fruit)):
    print(list_fruit[x])

for x in range(1, 11, 2): #1,3,5,7,9
    print(x)

print("Now we will get all details about your class: \n----------\n")
for i in range(3):
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))
    phone = input("Enter phone: ")
    print("Printing student number " + str(i+1) + " Details...\n")
    sleep(1)
    print("Full name: " + name + "\nAge: " + str(age) + "\nPhone: " + phone + "\n----------\n")

print("Bye bye")
