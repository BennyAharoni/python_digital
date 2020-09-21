def menu():
    while(True):
        choice = input("Menu:\n----------------\n1. Dogs Details\n2. Friends List\n3. Azzeret\nEnter your choice: ")
        if choice == "1":
            Dogs()
        elif choice == "2":
            Friends()
        elif choice == "3":
            num = int(input("Enter a number to calculate factor of it: "))
            print("Azzeret of " + str(num) + " is: " + str(Azzeret(num)))
        else:
            print("Enter 1 - 3 only!!!\n")
            continue
        exit = input("Do you want to exit? y/n: ")
        if exit == "y":
            break
        else:
            print("Welcome back!!!\n")
            continue
    print("Bye bye!")


def Dogs():
    name = input("Enter Dog's name: ")
    age = int(input("Enter dog's age: "))
    print("\nDogs name: " + name + "\nDog's age: " + str(age) + "\n")

def Friends():
    list_friends = []
    for i in range(5):
        list_friends.append(input("Enter a friend's name: "))
    name = input("Enter new name: ")
    if name in list_friends:
        print(name + " is inside the list\n")
    else:
        print(name + " isn't inside the list\n")


def Azzeret(x):
    if(x <= 1):
        return 1
    return x * Azzeret(x - 1)

menu()