#conditions

a = input("Enter a name: ")
if a == "Benny":
    print("Hello, Benny!")
    AGE = int(input("Enter your age: "))
    if AGE >= 54:
        print("Wow, you are greater than 54 y.o.")
    else:
        print("You are too young")
else:
    print("Where is Benny?")
    print("Bye bye")

number = int(input("Enter a number"))
if number > 6 or number != 10:
    print(number * 2)
else:
    print(number - 1)